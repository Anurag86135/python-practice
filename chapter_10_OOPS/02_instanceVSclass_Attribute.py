class Employee:
    language="python"# this is class Attribute
    salary=12344555


Anurag=Employee()

Anurag.language="javascript" # this is an instance Attribute
print(Anurag.language,Anurag.salary)


#keep this in mind--> Instance Attribute take preferencesover class Attibutes during assignment and retrival