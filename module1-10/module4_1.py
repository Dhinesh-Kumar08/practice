'''testprogram'''

a = 100

user = "John Doe"

import time

def square(x):
    return x*x

print(f"module4.py was invoked : a = {a}, user = {user}")
print(square(2))
print(f"module4_1.py is running as {__name__} module")  # __name__ is a "dunder" name