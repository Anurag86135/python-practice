#Can we have a set with 18(int) and '18'(string)
s=set()
s.add(18)
s.add('18')
print(s)
print(len(s))

# what will we the length of this code
# s=set()
# s.add(20)
# s.add(20.0)
# s.add('20')
# print(s)
# print(len(s))//here two returns because according to python property 20 and 20.0 are same it does not consider the data type

# what is the type of s if
s={}
print(type(s)) # it is a dictioary because {} is used to create dictionary


# Create an empty dictionary. Allow  4 friends to enter their favorite language as value and
#  use key as their names. Assume that the names are unique

# d={}
# for i in range(4):
    
#     name= input("Enter friends name :")
#     language=input("Enter favorite language :")
#     d.update({name: language})
# else:
#     print("Thank you")

# print(d)
# print(len(d))

# can you change the value inside a list which is contained in set S?
s={3,2,11,"hello bhao",[2,4]}
s[4][0]=8
print(s) # it will give an error because list is mutable and set is immutable
