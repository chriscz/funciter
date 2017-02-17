Functional style iterator and iterable maninulation for python.

Description
-----------
`Sequence` instances can be backed by either iterators or iterables.
When an iterable object is used, the instance will be reusable.

However if an iterator is used, then the instance is depletable and can
only be used once.

Each operation on the instance returns a new `Sequence` instance
that does not affect the original (this is not the case when an iterator was passed
during construction).

Look at `usage.py` for some examples of its use.

Known Issues
------
- No caching of iterated values, therefore the whole chain of transformation is 
  applied every time the iterator is restarted.

