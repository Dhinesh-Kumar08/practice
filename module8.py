#day 8 - july 12th
'''for loop
iterables,iterator and iteration protocol
collection as iterables
for loop - using range(),enumerate(),zip(),reversed()and sorted()
overview on itertools module'''

values = 12 , 34, 67, 85, 23, 89
for i in values:
    print("counting",i)

print(iter(values))
print("\n")
no_int = int(input("enter no times"))
user_inputs = []
for i in range(1,no_int+1):
    inp = input(f"enter line {i} :")
    user_inputs.append(inp)
print(user_inputs)

print("\n")
user_inputs = []
while (inp := input(f"Enter a line or press enter to end :")):
    user_inputs.append(inp)
    
print(user_inputs)

a = str(input("enter the string : "))
print(iter(a))
for c in a:
    print(f"c = {c}")

#if use int it is not iterable
print("\n")
values = 12, 34, 56, 78
ti = iter(values)
print(ti)

print("\n")
n = int(input("Enter a value: "))
print(f"the square of {n} is {n*n}")


try:
    a = int(input("enter a value: "))
    b = int(input("Enter another value: "))
    c = a/b
except ValueError:
    print("Got an invlaid input. Please type a valid number.")
except ZeroDivisionError:
    print("second value must not be zero")
else:
    print(f"square of {c} is {c*c}")

print("End of program")    

print("\n")
n = int(input("end: "))
start = int(input("start: "))
for i in range(start,n+1):
    print("counting",i)
    
a = range(0,20,2)
print(a,"\n",type(a))
for v in a:
    print(v)
    

start = int(input("Enter start value: "))
times = int(input("Enter how many times: "))
if times <=0:
    step = -1
else:
    step = 1


stop = start+times
for v in range(start,stop,step):
    print("counting",v)

for v in range(20,10,-1):
    print(v)
    

players = "john","adrian","jones", "bourne","steve"
scores = 45,34,78,23,12

for p in players:
    print(f"Players: {p}")
    
for s in scores:
    print(f"scores: {s}")
    

players = "john","adrian","jones", "bourne","steve"
scores = 45,34,78,23,12
for i in range(0,len(players)):
    print(f"{players[i]} scored {scores[i]}")
    
print("\n")
players = "john","adrian","jones", "bourne","steve"
scores = 45,34,78,23,12

z = zip(players, scores)
print(z,type(z),iter(z))
print(next(z))
print("\n")
#parallel iteration using zip
players = "john","adrian","jones", "bourne","steve"
scores = 45,34,78,23,12
for p,s in zip(players, scores):
    print(f"{p} scored {s}")
    
    
for r in zip(players, scores):
    print(f"r= {r}")
    
players = "john","adrian","jones", "bourne","steve"
for i in range(len(players)):
    print(f"i = {i}, players = {players[i]}")
    
for i,p in enumerate(players):
    print(i, p)