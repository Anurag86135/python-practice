#3) A spam comment is defined as a text containing following keywords
# "Make a lot of money","buy now","subscribe this", "click this".write a program to detect the spams

# p1="Make a lot of money"
# p2="buy now"
# p3="subscribe this"
# p4="click this"

# message =input("Enter your comment: ")

# if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
#     print ("This comment  is a spam")
# else:
#     print("this comment is not a spam")

# 4) Write a program to find whether a given username contains less than 10 characters or not.

username=input("Enter username : ")

if(len(username)<10):
    print("your username contains less than 10 character ")
else:
    print("your username contains equal to or more than 10 character")


