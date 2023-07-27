#day18
#using set and dict datatypes
a = {56,23,89,12,63,29}
b = {54,23,78,12,89,32}
c = {89,56,29}
result = a-b
print(result)
print(b-a)

print(a&b)
print(a | b)
print(a^b)
print(c < a)
print(c < b)
print(a > c)


a = [10, 20, 30, 20, 30, 40, 50, 20, 30, 40, 20, 67, 54, 20, 10, 20, 56, 54]
print(set(a))


a = [10, 20, 30, 20, 30, 40, 50, 20, 30, 40, 20, 67, 54, 20, 10, 20, 56, 54]
b = list(set(a))
print(b)

#today-26/07/2023
a = {23,44,56,21,67,88,99,32,10}
print(a)
a.add(100)
print(2)
a.remove(10)
print(a)
print()
a = {23,44,56,21,67,88,99,32,10}
print(a)

b = {55,66,77,88}
a.update(b)
print(a)

print()
a = {23,44,56,21,67,88,99,32,10}
v = a.pop()
print(f"Popped {v=}, {a=}")

v = a.pop()
print(f"Popped {v=}, {a=}")
print()

v = a.pop()
print(f"Popped {v=}, {a=}")
while a:
    v = a.pop()
    print(f"popped {v=} {a=}")

print()

a =[]
print(a,type(a))

b ={}
print(b,type(b))

c ={}
print(c,type(c))

d =set()
print(d,type(d))
print()
a = {23,44,56,21,67,88,99,32,10}
print(a)
b = a.copy()
print(a,b)
print(id(a),id(b))
print()


#a set is amutable

a = "this is a test string"
b = "this is a test string"
print(id(a),id(b))
a==b
print(hash(a),hash(b))

#for an o
#a ={10,20,{30,40,50}, 60}
#print(a)

#another type of set without modify and insert new
#frozenset

print()

#dictionary - borow most of the features of a set.
#keys of a dictionay must be hashable and unique
#before python 3.6,dictionary were unordered.

a ={"name":"john", "dept":"IT","place":"mumbai"}
print(a,type(a))
print(len(a))

print("dept" in a)
print()
for e in a:
    print(e,end="\n")
    
a ={"name":"john", "dept":"IT","place":"mumbai"}
print(a["dept"])#using non-existent keys for subscripting a dictionary - rasie a key error'
a = {"name": "John", "dept": "IT", "place": "Mumbai"}
key = "Dept"
if key in a:
    print(a[key])
else:
    print(None)

print(a.get(key)) # The .get() method returns the value if a key exists, else -> None

a ={"name":"john", "dept":"IT","place":"mumbai"}
b = {"score": 4.5, "team": "team-b", "role": "developer", "place": "Bengaluru"}

print(a)

a.update(b)
print(a)