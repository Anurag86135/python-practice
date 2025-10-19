class Employee:
    def __init__(self):
        print(f"Constructor of Employee")
    a=1


class Programmer(Employee):
    def __init__(self):
        super().__init__()
        print("Constructor of Programmer")
    b=2


class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Constuctor of Manager class")
    c=3

obj= Manager()
print(obj.c) #if we want to call the constructor of the programmer class too with Manager class then we have to use super keyword
