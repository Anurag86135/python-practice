class Employee :
    a=1
    @classmethod # now due to this decorator output will 1
    def show(cls):
        print(f" The class attribut of a is {cls.a}")
    

e=Employee()
e.a=44
e.show()# yanha pe instance Attribute print hoga 44 but hame class attribute ko print kana hai