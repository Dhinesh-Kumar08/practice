#standard comparsion operators are:
# ==, !=, < , >, <= , >=
c = 50 <= 50
print(c,type(c),id(c))
#False <class 'bool'> 140732450249608
a =1234 #input("num1")
b = 1234 #input("num2")
print(a == b , a is b , a is not b)

values = 45,67,23,89,12,63,86,34,90
print(values,type(values))
asr = input("enter the number :")
for i in values:
    if i == asr:
        print(f"{asr} is there {values}")
    else:
        print(f"{asr} is not there {values}")