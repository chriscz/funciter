# XXX only used as an annotation
def _wrap_in_iter(function):
    def wrapped(*args, **kwargs):
        item = function(*args, **kwargs)
        # prevent unnecessary wrapping
        if not isinstance(item, FunctionalIterator):
            item = FunctionalIterator(item)
        return item

    return wrapped

class FunctionalIterator(object):
    """
    A more functional way of accessing and using iterables
    """
    sentinel = object()

    def __init__(self, iterable=None):
        self._iterable_item = iterable or []

    @property
    def _iterable(self):
        return self._iterable_item

    def head(self):
        for i in self[0:1]:
            return i

    @_wrap_in_iter
    def tail(self):
        return self[1:]

    def last(self):
        last = self.sentinel
        for i in self:
            last = i

        if last is self.sentinel:
            raise ValueError('empty iterable')
        else:
            return last

    @_wrap_in_iter
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

    @_wrap_in_iter
    def take_while(self, predicate):
        for i in self:
            if predicate(i):
                yield i
            else:
                return

    @_wrap_in_iter
    def take(self, count):
        return self[:count]

    @_wrap_in_iter
    def drop(self, count):
        return self[count:]

    @_wrap_in_iter
    def __getitem__(self, item):
        if not isinstance(item, slice):
            item = slice(item, item + 1, 1)

        if item.step is None:
            item = slice(item.start, item.stop, 1)

        if item.start is None:
            item = slice(0, item.stop, item.step)

        if item.stop is None:
            item = slice(0, item.stop, item.step)

        if item.step < 0:
            raise ValueError('slice step < 0')

        iterator = iter(self)

        # skip
        for i in xrange(0, item.start):
            try:
                iterator.next()
            except StopIteration:
                raise ValueError('too few elements in iterable')

        # collect
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

    def __iter__(self):
        for i in self._iterable:
            yield i
