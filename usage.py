from __future__ import print_function
from funciter import Sequence
from funciter import IteratorAlreadyStarted

# since these are `iterables` and NOT iterators,
# we can reuse our constructer iterator
A = range(11)
B = "cats like catnip"

# ------------------------------------------------------------------------------ 
# 1. use it like a normal iterator
# ------------------------------------------------------------------------------ 
for i in Sequence(range(5)):
    print(i)

# ------------------------------------------------------------------------------ 
# 2. Filter certain elements
# ------------------------------------------------------------------------------ 
cats_only = Sequence(B).filter(lambda x: x in 'cat ')
print(''.join(cats_only))

# it's reusable because it's backed by an iteraBLE
print("it works again! again!")
for x in cats_only:
    print(x)

# ------------------------------------------------------------------------------ 
# 3. Skip the even elements
# ------------------------------------------------------------------------------ 
Ai = Sequence(A)[1::2]
for i in Ai:
    print(i)

# again, since it's backed by a iterable, it's reusable    
for i in Ai:
    print(i)

# ------------------------------------------------------------------------------ 
# 4. Apply another operation to the sequence
# ------------------------------------------------------------------------------ 
print("skip the first odd element (1)")
Qi = Ai[1:]

for i in Qi:
    print(i)

# ------------------------------------------------------------------------------ 
# 5. what about a depletable source?
# ------------------------------------------------------------------------------ 

# x is now a sequence backed by an iteraTOR    
x = Sequence(_ for _ in range(10)) 

# Either s or e can be used, but not both, since
# they are backed by the same iteraTOR
s = x[::2] 
e = x[::3]

# Consume the first element of `s` 
for i in s:
    print(i)
    break

# Let's try using `e`
try:
    for i in e:
        print(i)
except IteratorAlreadyStarted as e:
    print(e)
    print("yup, started iterators can't be reused!")
else:
    raise RuntimeError('Expected an exception to be raised, but none was!')

# ------------------------------------------------------------------------------ 
# 6. Another iteraTOR example
# ------------------------------------------------------------------------------ 
x = Sequence(_ for _ in range(10))
e = x[::3]

ei = iter(e)

print("HEAD", e.head())

# Cannot start again!
try:
    x[::2].filter(lambda x: x > 0)[0]
except IteratorAlreadyStarted as e:
    print(e)
else:
    raise RuntimeError('Expected an exception to be raised, but none was!')

try:
    for i in ei:
        print(i)
except IteratorAlreadyStarted as e:
    print(e)
else:
    raise RuntimeError('Expected an exception to be raised, but none was!')
