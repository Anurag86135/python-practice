# 6)# Write a program which finds out whether a given name is present in alist or not.
# list=["harry","Anurag","Yash","Mohan"]
# name=input("Enter your name : ")

# if(name in list):
#     print("yes it is present")
# else:
#     print("Not present in present")

# 7) ?write a program to czlculate the grade of a student from his marks from the following scheme:

# marks=int(input("Enter your marks : "))

# if(marks>=90 and marks<=100):
#     print("Grage -> Ex")
#     Grade='Ex'
# elif(marks>=80 and marks <90):
#     Grade ="A"
# elif(marks<80 and marks>=70):
#     Grade="B"
# elif(marks<70 and marks>=60):
#     Grade ="c"
# elif (marks<60 and marks >=50):
#     Grade ='D'
# elif(marks<50):
#     Grade="f"

# print(Grade)

#  Write aprogram to find out wether a given post is tlking about "Anurag or not".

# post =" hey Dear Anurag Congratulation!  you are selected in Microsoft as an software Engineer "
post=input("Enter your post")

if("Anurag".lower() in post.lower()):
    print("yes this post is talking about Anurag")
# elif("Anurag" in post):
#     print("yes it is present") don;t need of this if we use lower function
else:
    print("not talking about Anurag")