class Employee:
    a=1

    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self,value):
        self.fname=value.split(" ")[0]
        self.lname=value.split(" ")[1]


#by this program we also can understand encapsulation and Abstraction .

e=Employee()
e.a=45

e.show()


e.name="Anurag Mishra"
print(e.fname,e.lname)