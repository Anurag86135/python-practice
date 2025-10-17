#3) Create a class with a class Atribute a; create an object from it and set 'a' directly using object.a=o.Does this change the class Attribue.
# class Demo:
#    a=4

# o=Demo()
# print(o.a)# prints the class attribute because instance attribute is not present
# o.a=0
# #instance attribute is set

# print(o.a) # Prints the instance attribute because instance attribute is present

# print(Demo.a)#Prints the class atrribut

# # Ans->> no this dont change the class attribute.


#4) Add a static method in problem 2, to greet the user with hello:
class Calculator:

    def __init__(self,n):
        self.n=n
    
    @staticmethod
    def greet():
        print("Hello sir🙏")
        
    def square(self):
        print(f"The square of number {self.n} is {self.n *self.n}")
    
    def Cube(self):
        print(f"The cube of the given number {self.n} is {self.n*self.n*self.n}")

    def squareRoot(self):
        print(f"The SquareRoot of the given number {self.n} is {self.n**0.5}")

Calculator.greet()

num=int(input("Enter the number: "))

a=Calculator(num)
a.square()
a.Cube()
a.squareRoot()
