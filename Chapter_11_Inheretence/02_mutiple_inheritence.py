class Employee: # multiple inheritence
    company="TCS"
    name="Default name"
    def show(self):
        print(f"The name of the employee is{self.name} and the company is {self.company}")


class Coder:
    language ="Python"
    def printlanguage(self):
        print(f" out of all the languags heere is your language: {self.language}")


class Programmer (Employee , Coder):
    company ="Microsoft"
    def showlanguage(self):
        print(f"The name is {self.company} and he is good with {self.language} language")

a=Employee()
b=Programmer()

b.show()
b.printlanguage()
Employee.show(a)
b.showlanguage()