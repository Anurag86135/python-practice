class Employee:# Multilevel inheritence
    a=1

class Programmer(Employee):
    b=2

class Manager(Programmer):
    c=3


obj=Employee()
print(obj.a)# prints the a attribute
# print(o.b)# shows an error as threr is no b attribute in Employee class

obj=Programmer()
print(obj.a,obj.b)

obj=Manager()
print(obj.a,obj.b,obj.c)
