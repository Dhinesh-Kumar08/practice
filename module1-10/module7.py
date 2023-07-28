#day 7
#using the while loop
#Using break and continue statement 
#using for loop

a = "hello"
if a:
    print("true...")
else:
    print("false...")
    

name = input("enter your name: ")
if not name:
    print("you must type a valid name...")
else:
    print(f"hello {name}")
    
v = int(input("Enter a postive number between 0 and 10: "))
if v>=0 and v<=10:
    print("processing value: ",v)
else:
    print("the value is out of range...")
    
a = "hello {0}, welcome to {1}"  
name , place = "surya","akm"
print(a.format(name,place))
print(f"hello {name},welcome to {place}")

v =12
print(f"v = {v}")
print("v in decimal = {0}, in hex = {0:x}, in binary = {0:b} , in octal = {0:o}".format(v),"\n")
print(f"v in decimal = {v}, in hex = {v:x}, in binary = {v:b}, in octal = {v:o}")

#the"while" loop is a conditional looping statement
v = 2 
if v >= 5 or v % 2 == 0 :
    print("\n","got a valid number")
    
    
v = int(input("enter the number the loop get work: "))
while v < 5:
    v = int(input("enter a vaild number greater than 5: "))

print(f"got a value: {v}")

print("\n")
v = 0 
while v < 5:
    print(f"v = {v}")
    v += 1

print("\n")

for v in range (5):
    print(f"v = {v}")
    
#use "while" loop for non deterministric iteration
#before-hand how many times you will need to repeat run some statement

#use "for" loop for deterministric iteration (that, you know very well how many)
#time you need to repetitively run some statements


a = 10, 20, 30
print(a,"\n", type(a))

#A tuple is an immutable sequence of items


a  = "Hello World"
print(a.upper())
print(a.swapcase())
print(a)

a = [10,20,30]
print(a,"\n",type(a))

a = 10, 20, 30
print(a,"\n",type(a))
a = 40, 50, 60
print(a,"\n",type(a))

#A list is a mutable equvalent of a tuple
a = [10, 20, 30]
print(a[0])
a[0]=15
print(a)
a.append(40)
print(a)
v = a.pop()
print(f"v={v}, a={a}")


values =[]
while (v := int(input("enter  a value (0 or end): "))):
    values.append(v)
    print(f"{values=}")
    
print("\n")
print(f"loop complete : {values=}")

total = 0

while values:
    v= values.pop()
    print(f"{v=}, {values=}")
    total += v
    print(f"{v=}, {values=}, {total}")
    
print(f" total of list = {total}, {values=}")


values = [55,67,-32,67,-89,76,23]
total = 0
corrupt = False

while values:
    v = values.pop()
    if v < 0:
        print("Got a negative, data is corrupt, bailing out!")
        corrupt = True
        break
    total += v
    
else:
    print("\n")
    print("Accumulated total = ",total)
    
    
    
rec = 10, False, 6.7,"hello",(33,44,55)
print(rec)

rec1 = list(rec)
print(rec1, type(rec1))

rec2 = tuple(rec)
print(rec2, type(rec2))


v = rec1.pop()
print(v, rec1)