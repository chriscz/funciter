from __future__ import print_function
from functy import Sequence as I
from functy import IteratorAlreadyStarted

# since these are `iterables` and NOT iterators,
# we can reuse our constructer iterator
A = range(11)
B = "cats like catnip"

# use like a normal iterator
for i in I(range(5)):
    print(i)

# only allow certain elements through
cats_only = I(B).filter(lambda x: x in 'cat ')
print(''.join(cats_only))

print("it works again! again!")
for x in cats_only:
    print(x)

# skip even elements
Ai = I(A)[1::2]
for i in Ai:
    print(i)

print("Look ma, reusable!")    
# Resusable?
for i in Ai:
    print(i)


print("skip the first")
Qi = Ai[1:]

for i in Qi:
    print(i)
print("reusable, again!")

# what about a depletable source?
x = I(_ for _ in range(10))
s = x[::2]
e = x[::3]

for i in s:
    print(i)
    break

try:
    for i in e:
        print(i)
except IteratorAlreadyStarted as e:
    print(e)
    print("yup, started iterators can't be reused!")

# test remaining case
x = I(_ for _ in range(10))
e = x[::3]

ei = iter(e)

print("HEAD", e.head())

# Cannot start another one!
try:
    s = x[::2].filter(lambda x: x > 0)[0]
except IteratorAlreadyStarted as e:
    print(e)

try:
    for i in ei:
        print(i)
except IteratorAlreadyStarted as e:
    print(e)
