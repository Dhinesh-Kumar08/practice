#day 2
a = 100
print("Hello World")
#syntax error
print("start")
#a =
100
print("end")
#type error
print("start")
#100 + "200" 
print("end")
#compound statement
'''for v in 1,2,3,4:
print(v)
output:
1
2
3
4'''
a = 10
#indentationerror
if a>5:
    print("the value is large")
    print("this is another test message")
#about pep and pep - 8
#https://peps.python.org/pep-0008/

#simple assignment
a = 1234 #this is a simple assignment
        #1234 is literal data
a  = 15 * 45 + 3 # that assign the expression to variable

#the technically called a 'name' in python
#commonly known as variable names, or variables in short
'''variable starts at {A-Z,a-z},{1-9} and _'''

player_score = 1234
print(player_score) 

a = 1234
b = a
print(a, b)
#1234 1234
a = 4321
b = a
print(a, b)
#4321 4321
b = 8976
print(id(a) ,id(b))
#output
#2297283132400 2297283133008
del a
print(a , b)