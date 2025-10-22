#Create two virtual environments, install few packages in the first one. How do you create a similar environment
#in the second one ?
# 2) Write a program to input name, marks and phone number of a student and format it using the format function like below:
# "the name of the student is Anurag, his marks are 72 and phone number is 9898989"

# name=input("Enter your name please : ")
# marks=int(input("Enter your marks : "))
# Phone=int(input("Enter your current and running phone number : "))


# about="The name Of the Student is {1} , his marks are {2}  and phone number of a student is {0}".format(Phone,name, marks)
# print(about)


# 3)A list contains the multiplication table of 7. write a program to convert
#  it to vertical string of same numbers.
# table=[str(f"{7} X {i} = {7*i}") for i in range(1,11)]
# s="\n".join(table)
# print(s)

# 4)Write a program to filter a list of numbers which are divisible by 5
from functools import reduce


l=[10,2,33,45,65,66,78,80]

# divisible=lambda x:x%5==0

# result=list(filter(divisible,l))
# print(result)


# 5)Write a program to find the maximum of the numbers in alist using the reduce function.
# def greater(a,b):
#     if(a>b):
#         return a
#     return b


# print(reduce(greater,l))


# 6) Run pip freeeze for the system interpreter. take the contents and create a similar virtualenv.

#7)Explore the Flask module and create a web server using Flask &python

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
app.run() # flask is used to make api or websites