
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a//b

print("Enter your choice that what you wnated to do : ")
print("1. for Addition")
print("2. for substraction")
print("3 . for multiplication")
print("4 . for division")

choice=int(input("Enter your choice 1/2/3/4"))

a=float(input("Enter first number :"))
b=float(input("Enter Second number: "))

if choice ==1:
    print(f" Addition of the numbers {a} and {b} is {add(a,b)}")
elif choice==2:
    print(f" substraction of two numbers {a} and {b} is {sub(a,b)}")
elif choice==3:
    print(f" the multiplication of two numbers {a} and {b} is {mul(a,b)}")
else:
    print(f"the division is {div(a,b)}")

