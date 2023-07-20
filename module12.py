#day12-18th july
#topic-list method,String method and operation
a =[22,33,44,55,66,22]
print(a, type(a))
get = a.index(55),a.count(33)
print(get)
print("\n")
a = [11,23,56,76,43,89,21,54]
#a[2:2]=30
a.insert(2,30)
print(a, len(a))
print()
a = [11,23,56,76,43,89,21,54]
a.insert(20,60)
print(a)

#A list in python is implemented as a vector data structure
a = [10,20,30,40]
a.insert(0,35)
print(f"output ={a}")

#a.insert(len(a),50)
a.append(50)
print(a)
print()

a = [10,20,30]
b = [40,50,60]
a.append(b)
print(len(a))
print(a)
print()

#to extend on exiting list with element of another iterable , you can use extend() method
a = [10,20,30]
b = [40,50,60]
a.extend(b)
print(a)

a = [10, 20, 30]
a1 = a
b = [40,50,60]
print(a,a1, id(a),id(a1))
a = a + b
print(a, id(a))
print(a1)


a = [10, 20, 30]
a1 = a
b =[40, 50, 60]
print(a, a1, id(a), id(a1))
a += b
print(a, id(a))
print(a1)


a = [10,20,30,40,50]
del a[1]
print(f"{a=}")

v = print("Hello world")
print(v)

a = [10,20,30,40,50]
v = a.pop(1)
print(f"{a=}, {v=}")

score = 70
v = "pass" if score > 50 else "fail"

a =[]
b = int(input("enter the no of operation"))
for i in range(1,b+1):
    v = int(input("Enter value: "))
    a.append(v)
print(a)

s = input("Enter a word :")[:-1]
print(s)

a = [10,20,30,40,50,60,70,80]
#a.pop(a.index(30))
a.remove(30)
print(a)

while 30 in a:
    a.remove(30)
print(a)

a = [10,20,30,40,50,60]
b = a
a.clear()
#del a[:]
print(a, id(a))
print(b, id(b))

a = [10,20,30]
#s =a[:] old trick of copy of item in new variable
s = a.copy()
print(a)
print(s)

a = [10,[20,30], 40]
b = a.copy()
c = a
print(a,b)
print(a is b,a is c)
a[1][0] = 25
print(f" {a=}, {b=}")
a[1][1] = 45
print(f"{a=} {b=}")


from copy import deepcopy
a = [10,[20,30],40]
b = deepcopy(a)
print(f"{a=}, {b=}")
a[1][0] = 25
print(f"{a=}, {b=}")
print(a is b, a[0] is b[0])

a =[10,20,30,40,50]
print(a)
a.reverse()
print(a, id(a))

a =[10,20,30,40,50]
for v in reversed(a):
    print(v,end=" ")
print()
print(a)

b = a[::-1] #create a reverse-copy of a list
print(a, b)

a.reverse() #reverse a list in-place
print(a)

b = a.reverse #method - reverse(),sort(),clear(),remove()->all return none

a = [45,23,78,99,54,12,42,78]
print(a,id(a))
a.sort()#sort
print(a,id(a))

#list method: index(),count()
#insert(),append(),extend()
#pop(),remove(),clear()
#copy(),reverse(),sort()

#list comprehension
a = [10,20,30,40]
print(a)

b =[v*v for v in a] #map operation using list comphrension
print(b)

nums = 10,20,30,40,50
print(sum(nums))
a = [56, "34",11,"89","22",78]

print(sum(int(n) for n in a))

b = [v for v in a if type(v) is int]
print(b)

values = [56,23,12,78,94,27,89,24,18,6,9,17]
result = [n for n in values if n%3 ==0]
print(sorted(result))