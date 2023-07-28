#day9-13th

values = [55,66,45,34,54,34,345,45]
Total = 0
while values:
    if values.pop()<0:
        print(f"Bailing out as the list contains Negative values")
        break
    Total += values.pop()
else :
    print(f"Accmulated total = {Total}")
    
values = [55,66,45,34,54,34,345,45]
Total = 0
while values:
    v = values.pop()
    if v < 0:
        print(f"Bailing out as the list contains Negative values")
        break
    Total += v
else :
    print(f"Accmulated total = {Total}")
    
players = "emily","john","adam","charles","dave","jonesh"

for i,p  in enumerate(players):
    print(f"{i=}  -> {p=}")
    
s = "emily"
print(s)

s1 = s.upper()
print(s, s1)

players = ["emily","john","adam","charles","dave","jonesh"]
print(players, id(players))

#TODO:transfer all items of players to upper case

print(players, id(players))
print("\n")
#reverse
players = ["emily","john","adam","charles","dave","jonesh"]
for i in reversed(players):
    print(i)
print(iter(reversed(players)))
print(players)
p2 = players[::-1]
print(p2)
#another type of reverse
for i in players[::-1]:
    print(i)
    
print("\n")
#sort
for i in sorted(players):
    print(i)
    
values = [55,66,45,34,54,34,345,45]
for i in sorted(values):
    print(i,end=" ")
print("\n")
values2 = values[::-1]
print(values)
print(values2)

#to reverse an existing list in-place
values.reverse()
print(values)

#to iterate over a list / tuple or any sequence in reverse order
#without changing them or creating another copy..
for v in reversed(values):
    print(v,end=" ")
print()
s = "hello"
for v in s:
    print(v,end=" ")
print()
for v in reversed(s):
    print(v, end=" ")
print("\n")
a = str(input("enter the string: "))
if a == a[::-1]:
    print("it is palindrome")

    print(f"the condition is:",a == a[::-1])
else:
    print("its not palindrome")
    
print("\n")

values = 56, 12, 54, 22, 89

s =sorted(values) #always creates a sortted list copy of original collection
#though sorted() works on all collection, if expect all items of the
#collection to be of the same type and must be comaparable
print(values)
print(s)

import itertools
a = [10, 20, 30, 40]
b = [50, 60, 70, 80]
for v in a+b:
    print(v)
print("\n")
print("using of itertools")
for v in itertools.chain(a,b, range(10,20), zip(a,b)):
    print(v)
    

a = 1234
b = 0x12f#hexdecimal
c =0o776#octal
d =0b1011#binary
print(a,b,c,d)
print(str(a),hex(b),oct(c),bin(d))

a = 100
print(a)
print(str(a))#the default string notation of an integer will use decimal format

print(hex(a),oct(a),bin(a),end=" ")#return hexdecimal string representation of an intger

a =100
print(f"{a}, {a:x}, {a:o}, {a:b}")

a = 123
b = str(a)
print(a,b)
print(type(a), type(b))