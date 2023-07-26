def testfn():
    print("Start of testfn...")
    yield 100
    print("Back to testfn...")
    yield "hello world"
    print("Back again inside testfn...")
    yield
    print("End of testfn...")
    

g = testfn()
g#A generate is an iterable + iterator object
iter(g)

from time import sleep

def fib_gen(x):
    a, b =0, 1
    for v in range(x):
        yield a
        sleep(1)
        a, b= b, a+b

#g = fib_gen(10):
#for v ing :
for v in fib_gen(10):
    print(v, v*v)
    
    
'''output
0 0
1 1
1 1
2 4
3 9
5 25
8 64
13 169
21 441
34 1156'''
print("\n")


a = [10,20,30,40]
for v in a:
    print(v)
    
    

def foo():
    for i in range(10):
        sleep(1)
        print("foo: counting", i)

def bar():
    for i in range(10):
        sleep(1)
        print("bar: counting", i)

foo()
bar()
print()
#if use yield
def foo():
    for i in range(5):
        sleep(1)
        print("foo: counting", i)
        yield

def bar():
    for i in range(7):
        sleep(1)
        print("bar: counting", i)
        yield

g1 = foo()
g2 = bar()
tasks = [g1, g2]

from itertools import zip_longest
for _ in zip_longest(*tasks):
    pass


while tasks:
    for t in tasks:
        try:
            next(t)
        except StopIteration:
            tasks.remove(t)
            
            
            
a = [11,22,33,44,55,66,77,88,99]

def slow_square(x):
    sleep(0.5)
    return x*x
print(a)
b =[slow_square(v) for v in a]
print(b)

def my_range(*args):
    start, step = 0, 1
    
    if len(args) == 1:
        stop = args[0]
    elif len(args) == 2:
        start, stop = args
    elif len(args) == 3:
        start, stop, step = args
    else:
        raise TypeError("Invalid parameters passed.")

    while start < stop:
        yield start
        start += step

for v in my_range(10):
    print(v, end=" ") # OUT: 0 1 2 3 4 5 6 7 8 9
print()

for v in my_range(10, 20):
    print(v, end=" ") # OUT: 10 11 12 13 14 15 16 17 18
    

import random
random
print()

a = [34,12,78,93,24,67]
b = {34,12,78,93,24,67}
print(a, type(a))
print(b, type(b))

#A set
print(len(a))
print(len(b))
print(50 in a)


a = [34,12,78,93,24,67]
b = {34,12,78,93,24,67}
print(a[3])
print(b(3))

a = list(range(1000))
#%timeit 999 in a #in colab

#https://www.youtube.com/@raymondhettinger9603
#https://www.youtube.com/watch?v=9zinZmE3Ogk&list=PLRVdut2KPAguz3xcd22i_o_onnmDKj3MA&index=4