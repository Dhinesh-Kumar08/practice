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