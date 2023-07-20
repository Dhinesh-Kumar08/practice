
#notation of an object by assign value on it
a = 1234
b = 1234
c = a
print(a, b, c)
print(id(a) ,id(b) , id(c))
#comparision expression (check)
print(a==b)
print(a == c)
print(a is b,a is c, a ==b, a==c)
#"is"
print(id(a),id(b),id(c))
a = 123
b = 123
c = 123
print(id(a),id(b),id(c))

a = "hello world"
b = "hello world"
print(a is b)
#all word-string are interned in python
'''true'''
a = 123+4j
b = "hello" #when we assign some type of data or value
'''<class 'complex'> (type of "a")
<class 'str'> (type of "b")'''
print(type(a),"\n",type(b))

a = 3+4j
b = 2j
print(a+b)
print(a.real,b.imag)
print(b.real,b.imag)
''' 3.0 2.0
    0.0 2.0'''
    
#simple asignment
a = 10

#tuple packing
a = 10,20.2, "test"
print(a, type(a))

#A tuple is a immutable sequenced collecting of items

print(a)
print(a[0],"\n",a[1])
# when we using out range index were it shows error 
a = int(input())
for i in range(1,a+1):
    print(i)



a =10 ,20 , 30
print(a, type(a))
b , c , d = a  #unpacking the tuple
print(b,c,d)

a = tuple([x*x for x in range(100)])
print(a[3])
print(a[2])


#parallel assignment
a,b  = 10, 20
print(a,b)
a, b = b, a
print(a,b)

#Augmented assignment
a = 10
a+=5
#15
print(a)
a-=2
print(a)
a*=2
print(a)
a//=5
print(a)

a = 10
#b += a += 5 
#    b += a += 5 
#           ^^
#SyntaxError: invalid synta
print(b)

#assignment chainloading
a = b = c = d = 1234
print(a, b, c, d)
print(id(a),id(b),id(c),id(d))

a = 10 >15
print(a)
#walrul assignment - intro in python 3.8
print((a:=10) >15) # :-), :-/, :-(, :-D ,:=
'''false'''
print(a)
'''10'''
