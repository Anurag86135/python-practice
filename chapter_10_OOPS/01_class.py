class employee:
    language="Python" # This is a class Attribute
    salary=12000000


harry=employee()
harry.name="Anurag" # This is an instance/object attribute
print(harry.name,harry.language,harry.salary)

rohan=employee()
rohan.name="Rohan ji"
print(rohan.name,rohan.salary,rohan.language)

# here name is instance/object attribute and salary and language are class attribute
#  as they directly belong to the class