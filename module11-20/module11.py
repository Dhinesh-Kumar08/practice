#day11
#topic-list and tuple method,string method and operations

a = [10,20,30,40,50,60,70]
print(a[2:5])
print()

a = [10,20,30,40,50,60,70]
a[1] = 45
print(a)

a = [10,20,30,40,50,60,70]
a[1:4] =11,36,78,89,14,55
print(a)
print()

a = [10,20,30,40,50,60,70]
a[1:4] = range(100,150,5)
print(a)

a = [10,20,30,40,50,60,70]
a[1:4] = "hello"
print(a)
print()

a = 10,20
print(a, type(a))

a = 20
print(a,type(a))
print()

a = [10,20,30,40,50,60,70]
a[3:3] = 32,25,37
print(a)

a = [10,20,30,40,50,60,70]
del a[3]
print(a)

a = [10,20,30,40] # creating a list using literal notation
a = list(range(10,100,10)) #creating a list using the list() constructor

print(a)

print(list)
print()

print(tuple(range(10,100,10)))


a = "hello"
print(a)

b = list(a)
print(b)

c = tuple(a)
print(c)

d = str(a)
print(d)

print()

l = [10,True,5.6,(11,22,33)]
s = str(l)
print(s)

import datetime
print(str(datetime))
print()

a = [10,20,30,40]
#int(a)#in the face of ambiguity.refuse the temparture to guess



a =list(range(10,100,10))
print(a)
print()
print(a[:-1:2], a[1::2])
del a[::2]
print(a)


a =list(range(10,100,10))
print(a)
a[1::2] = a[:-1:2]#doubt
print(a)

a = list(range(10,110,10))
print(a[1::2],a[::2],a[:-2:2])
#todo -> 10,20,30,40,50,40,30,20,10
print()
a[5:] = a[4::-1]
print(a)
print()

a = 56,32,56,77,87,12,34,21,65,55,32,77,23,12,77,21,77,89
print(a.index(12))
print(sorted(a))


def find_indices(t,v):
    i =0
    try:
        while True:
            i = t.index(v,i)
            print(i,end=" ")
            i += 1
    except ValueError:
        pass


a = 56,32,56,77,87,12,34,21,65,55,32,77,23,12,77,21,77,89
find_indices(a ,77)
#out[3,11,14,16]


