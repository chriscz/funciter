# XXX only used as an annotation
from functools import partial, wraps

class IteratorAlreadyStarted(RuntimeError):
    pass

def _wrap_in_iter(generator=False):
    def wrap(function):
        @wraps(function)
        def wrapped(*args, **kwargs):
            if generator:
                return Sequence(partial(function, *args, **kwargs))
            else:
                item = function(*args, **kwargs)
                # prevent unnecessary wrapping
                if not isinstance(item, Sequence):
                    item = Sequence(item)
                return item
        return wrapped
    return wrap

def _canonical_slice(item):
    start = item.start or 0
    stop = item.stop
    step = item.step or 1

    item = slice(start, stop, step)

    if item.step < 0:
        raise ValueError('slice step < 0')
    return item

class Iterator(object):

    def __init__(self, iter_instance, iterator):
        """
         Arguments
         ---------
         iterator: Iterator
        """
        self.iteri = iter_instance
        self.iterator = iterator

    def __iter__(self):
        return self

    def next(self):
        """
        This extra class is necessary to intercept the `next()` call, 
        since there was a problem where a generator could be started,
        and thus yield the first value, and a sibling generator
        could also be started and yield a value. Originally the 
        idea was to do the following in Iter.__iter__.

        try:
            yield iterator.next()
        except StopIteration:
            return
        finally:
            self.started = True

        note the self.started will only be set when the generator's next() was
        called. In the case of the generator, we cannot tell when the iterable is actually consumed, 
        but using a seperate iterator calls, the next() call would indicate actual consumption
        """
        self.iteri.started = True
        # replace with the consequent next function for the sake of speed!
        self.next = self.continued
        return self.next()

    @wraps(next)
    def continued(self):
        return self.iterator.next()

class Sequence(object):
    """
    A more functional (and pythonic) way of consuming iterables and iterators, i.e.
    restartable and non-restartable sequences.
    """
    sentinel = object()

    def __init__(self, iterable=None):
        self._iterable_item = iterable or tuple()
        self.started = False
        self.is_iterator = False

    @property
    def _iterable(self):
        if self.is_iterator and self.started:
            raise IteratorAlreadyStarted("Iterator has already been started!")
        try:
            # NOTE for iterators, iter() returns the same iterator
            iterator = iter(self._iterable_item)
            if iterator is self._iterable_item:
                # XXX what about special case where a class
                # returns itself as the iterator? is that possibly?
                self.is_iterator = True
            return iterator
        except TypeError:
            # XXX Assume it is callable and thus a generator
            return self._iterable_item()
    
    def head(self):
        for i in self[0:1]:
            return i

    def tail(self):
        return self[1:]

    def last(self):
        last = Sequence.sentinel
        for i in self:
            last = i

        if last is Sequence.sentinel:
            raise ValueError('empty iterable')
        else:
            return last

    @_wrap_in_iter(generator=True)
    def filter(self, predicate_function):
        """
        filtered iteration support
        Parameters
        ----------
        predicate_function: function(x) -> bool

        Yields
        ------
        LinkedListNode
            elements for which predicate_function returns True

        """
        for i in self:
            if predicate_function(i):
                yield i

    @_wrap_in_iter(generator=True)
    def take_while(self, predicate):
        for i in self:
            if predicate(i):
                yield i
            else:
                return

    def take(self, count):
        return self[:count]

    def drop(self, count):
        return self[count:]

    @_wrap_in_iter(generator=True)
    def iter_slice(self, item):
        item = _canonical_slice(item)
        iterator = iter(self)
        # skip
        for i in xrange(0, item.start):
            try:
                iterator.next()
            except StopIteration:
                raise ValueError('too few elements in iterable')

        # iterate
        idx = item.start
        next = idx
        for i in iterator:
            if idx == next:
                yield i
                next = idx + item.step
            idx += 1
            if idx == item.stop:
                break

        if item.stop and idx != item.stop:
            raise ValueError('too few elements in iterable')

    def __getitem__(self, item):
        if isinstance(item, slice):
            return self.iter_slice(item)
        elif isinstance(item, (int, long)):
            return list(self.iter_slice(slice(item, item+1, 1)))[0]

    def __iter__(self):
        iterator = self._iterable
        return Iterator(self, iterator)
