#day15-21th july





def add_record(user, place,role):
    print(f"{user=}, {place=}, {role=}")


add_record("smith","mumbai","admin")
add_record("smith","mumbai","admin")
add_record(user="smith",place="mumbai",role="admin")#calling function with keyword arguments
add_record("John",role="mumbai",place="admin")
add_record("john",role="Support",place="chennai")

print(10,20,30,sep=",")

print()
def add_record(user="Guest", place="bengalore",role="Developer"):
    print(f"{user=}, {place=}, {role=}")

add_record()
add_record(role="Marketing")
add_record(place="vellore")

s ="this is a test string test test repeated test string"
a ="test"
def find_all(main_str, substr):
    i,length,indices = 0,len(substr),[]
    while True:
        i = main_str.find(substr,i)
        if i== -1:
            break
        indices.append(i)
        i += length
    return indices

print(find_all(s, a))


def good_function(test_word, target_word):
    location = [p for p in range(len(test_word)) if test_word.startswith(target_word, p)]
    return location 

print(good_function(s,a))

def testfn(a, *c, b=20):
    print(f"{a=},{b=},{c=}")

testfn(10,110,130,160)
testfn(10,110,130,160,b=75)
print()

def store(name,place,role,dept):
    print(f"{name=}, {place=}, {role=}, {dept=}")

rec = {
    "role": "DevOps", 
    "place": "Bengaluru", 
    "name": "Smith", 
    "dept": "IT"
}

#(**) it denote the dictionary to function
#(**rec) = rec
store(**rec)


def testfn(**a):
    print(f"{a=}")
    
testfn()
testfn(x = 100,y = 56,name = "john", blah="blah blah")



def testfn(*args,**krgs):
    print(f"{args=}")
    print(f"{krgs=}")
    print("-" * 40)
    
testfn()
testfn(10, 20, 30)
testfn(x = 5,y = 32,z = 12)
testfn(10,20,z = 20,a = 40)




def square(x):
    if type(x) in (int,float,complex):
        return x*x
    elif type(x) in (str,list,tuple):
        return x * 2
    else:
        return None