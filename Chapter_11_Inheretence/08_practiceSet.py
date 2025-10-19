# # 1) Create a class (2-D vector ) and use it to create another class represting a 3-D vector

# class TwoDVector:
#     def __init__(self,i,j):
#         self.i=i 
#         self.j=j

#     def show(self):
#         print(f" the vector is {self.i}i + {self.j}j")


# class ThreeDVector(TwoDVector) :
#     def __init__(self,i,j,k):
#         super().__init__(i,j)
#         self.k=k
#     def show(self):
#          print(f"The vector is {self.i}i+{self.j}j+{self.k}k")

# a=TwoDVector(1,2)
# a.show()
# b=ThreeDVector(1,2,3)
# b.show()


#2) Create a class 'pets' from a class 'Animals' and further create 'Dog' from 'Pets'.Add a method 'bark' to class 'Dog'.
# class Animals:
#     pass

# class Pets(Animals):
#     pass

# class Dog(Pets):
#     @staticmethod
#     def bark ():
#         print("bhou bhou !😁@....")

# obj=Dog()
# obj.bark()


# 3) Create class 'Employee' and add salary and increment propertities to it.
# class Employee:
#     salary=234
#     increment=20

#     @property
#     def salaryAfterincrement(self):
#         return (self.salary+self.salary*(self.increment/100))
    
#     @salaryAfterincrement.setter
#     def salaryAfterincrement(self,value):
#         #value =new slary after increement
#         self.increment =((value/self.salary)-1)*100


# e= Employee()
# # print(e.salaryAfterincrement)
# e.salaryAfterincrement=280.8
# print(e.increment)

# 4) Write a class 'Complex ' to represent complex numbers ,
#  along with overloaded operators '+' and '*' which adds and multiplies them.


# class Complex:
#     def __init__(self,r,i):
#         self.r=r
#         self.i=i

#     def __add__(self,c2):
#         return Complex(self.r+c2.r,self.i+c2.i)
    
#     def __mul__(self,c2):
#         real =self.r * c2.r - self.i *c2.i
#         image = self.r*c2.i + self.i*c2.r
#         return Complex(real,image)
    
#     def __str__(self):
#         return f" the sum of complex numbers is {self.r} + {self.i}i"


# c1=Complex(1,2)
# c2=Complex(3,4)
# print(c1 + c2)
# print(c1*c2)


# Write a class vector representing a vector of n dimensions.Overload the + and *
# operaters which calculates the sum and the dot(.) product of sum
# class Vector:
#     def __init__(self ,x,y,z):
#         self.x=x
#         self.y=y
#         self.z=z

#     def __add__(self,other):
#         result=Vector(self.x + other.x ,self.y + other.y , self.z+ other.z)
#         return result
#     def __mul__(self,other):
#         result=self.x*other.x+self.y*other.y+self.z*other.z
#         return result

#     def __str__(self):
#         return f" Vector ({self.x},{self.y},{self.z})"
    

# #test the implementation
# v1=Vector(1,2,3)
# v2=Vector(4,5,6)
# v3=Vector(7,8,9) #same dimension vector

# print(v1+v2) # Output :vector(5,7,9)
# # print(v1*v2)#Output : 32

# print(v1+v3)
# print(v1*v3)

# Write a __str__ method to print the vector as follows
# 7i+8j+10K Assume the vector of dimension 3 for this problem.



# class Vector:
#     def __init__(self ,x,y,z):
#         self.x=x
#         self.y=y
#         self.z=z

#     def __add__(self,other):
#         result=Vector(self.x + other.x ,self.y + other.y , self.z+ other.z)
#         return result
#     def __mul__(self,other):
#         result=self.x*other.x+self.y*other.y+self.z*other.z
#         return result

#     def __str__(self):
#         return f" Vector {self.x}i+{self.y}j+{self.z}k"
    

# #test the implementation
# v1=Vector(1,2,3)
# v2=Vector(4,5,6)
# v3=Vector(7,8,9) #same dimension vector

# print(v1+v2) # Output :vector(5,7,9)
# print(v1*v2)#Output : 32

# print(v1+v3)
# print(v1*v3)


#7) Override the __len__() method on vector of problem 5 to display the dimension of th vector
class Vector:
    def __init__(self ,l):
        self.l=l

    def __len__(self):
     return len(self.l)
    
v1=Vector([1,2,3])#list hai
print(len(v1))