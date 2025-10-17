class Student:
    subject="Hindi"
    totalstudent=500

    def getInfo(self):
        print(f" The subject is {self.subject}. The total sudents are{self.totalstudent}")

    def greet(self):
        print("Good Morning")

    @staticmethod
    def play():
        print("iths time to play Let's go")


obj=Student()

obj.subject="Maths" # instance attribute

obj.getInfo()# it is same sa Student.getInfo(obj)

obj.greet()

Student.play()# calling of static method
