class Employee:
    language ="Python"
    salary =1220000

    def __init__(self,name,salary,language):# dundermethod which is automatically called
        self.name=name
        self.salary=salary
        self.language=language
        print("I am creating an object")

   
    @staticmethod
    def greet():
        print("Godd morning")


obj=Employee("Anurag",2400000,"Jvascript")

print(obj.name,obj.language,obj.salary)
Employee.greet()
