user = input("enter your name :")
if user == "chandra":
    print("Welcome pythonista!")
else:
    print(f"Welcome to python - {user}")

#enter your name :chandra
#Welcome pythonista!
#Enter your name: dhinesh
#Welcome to python - dhinesh
if (user := input("Enter your name: ")) == "chandra":
    print("Welcome Pythoninsta!")
else:
    print(f"Welcome to python - {user}")
