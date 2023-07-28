a =[10,20,30,40,50,60,70,80,90]
while True:
    v = int(input("Enter a value (or 0 to finish): "))
    if v == 0:
        break
    a.append(v)
    a.sort()
    print(a)
    

from bisect import insort
a =[10,20,30,40,50,60,70,80,90]
while True:
    v = int(input("Enter a value (or 0 to finish): "))
    if v == 0:
        break
    a.append(v)
    a.sort()
    print(a)
    