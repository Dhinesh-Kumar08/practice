#day10-14th july
#python builtin datatype->numbers,tuple and list operation
a = 4.9
print(a, type(a))
b = int(a)
print(b, type(b))

c = True
d = int(c)
print(d, type(d))

print(5 +2)
print(5 - 2)
print(5 * 2)
print(5/2)
print(5%2)
print(10/2)

print(5//2) #python specfic floor-div operator(floor of divison)

v = int(input("Enter a value: "))

for i in  range((v//2)+1):
    print("counting",i)
    
#2 to the power of 5
print(2**5) 
p= print
import math
p(math.sqrt(16))
print()
print(bin(0b1100 | 0b1001))#bitwise or operator -> |
p(bin(0b1100 & 0b1001))#bitwise and operator -> &
p(bin(0b1100 ^ 0b1001))#bitwise xor operator -> ^

num = int(input("Enter the number: "))
if num % 2 ==0:
    print(f"{num} is even number")
else:
    print(f"{num} is odd number")

a = 12 
print(bin(a),a)
b = a <<2
print(bin(b), b)

a = 10
b = 20
c = a+b
print(c)#a._add_(b)
print(a.__add__(b))
print(a.__sub__(b))
print(a.__mul__(b))
print(a.__divmod__(b))

#duck typing - alex martelli
a = 10
a.__add__(20)
print(a)
print()
a = 10,20,30
b = 40,50,60
print(a,b)
c = a + b
print(c)
print()

#reptition
a = 10,20,30
b = a * 5 #sequence repetition
print(f"{a=},{b=}")

a ="hello"
b = (a * 5)
print(f"{a=}, {b=}")

print()


#subscript operation 
a = 34,56,12,89,42,67,84,29,15,18
print(a[0])
print(a[1])
print(a[-1])
print(a[-2])


#etracting slices for sequence

a = 34,56,12,89,42,67,84,29,15,18
print(a[2:7])
print(a[1:-2])

a = "hello world"
print(a[3:8])

a = 34,56,12,89,42,67,84,29,15,18,78,93,45,69
start = int(input("enter start value: "))
stop = int(input("enter the end value: "))
print(a[start:stop])
print(a[8:2:-1])
print(a[::-1])

print()

a = 10,"hello",[100,200,300], None,5.6
print(a[0])
print(a[2])
print(a[2][0],a[2][1])

