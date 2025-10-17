#1) Create a class 'programmer' for storing information of few programers working at Microsoft.
# class Programmer:
#     company = "Microsoft"
#     def __init__(self,name,salary,pin):
#         self.name=name
#         self.salary=salary
#         self.pin=pin

# p=Programmer("Anurag",1200000,"482001")
# print(p.name,p.salary,p.pin,p.company)

# r=Programmer("Ram",999999999,482002)
# print(r.name,r.salary,r.pin,r.company)


#2) Writa a class "calculator" capable of finding square,cube and square root of a number.

class Calculator:

    def __init__(self,n):
        self.n=n
        
    def square(self):
        print(f"The square of number {self.n} is {self.n *self.n}")
    
    def Cube(self):
        print(f"The cube of the given number {self.n} is {self.n*self.n*self.n}")

    def squareRoot(self):
        print(f"The SquareRoot of the given number {self.n} is {self.n**0.5}")

num=int(input("Enter the number: "))

a=Calculator(num)
a.square()
a.Cube()
a.squareRoot()
