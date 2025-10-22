# # Write a program to open three files 1.txt,2.txt and 3.txt.If any these files are not present, 
# #  a message without existing the program must be printed prompting the same.

# with open("3.txt","w") as f:
#         f.write("hello bhaiyo kese ho")
# try:
#     with open("2.txt","r") as f:
#         print(f.read())
# except Exception as e:
#     print(e)
# try:
#     with open("3.txt","r") as f:
#         print(f.read())
# except Exception as e:
#     print(e)
# try:
#     with open("1.txt","r") as f:
#         print(f.read())
# except Exception as e:
#     print(e)

# print("thankyou")

# 2) Write a program to print third, fifth and seventh element  from a list enumerate function.
# list=[2,3,4,66,77,87,"Anurag"]

# for i,item in enumerate(list):
#     if i ==2 or i==4 or i==6:
#         print(item)

# 3)Write a list comprehension to print a list which contains the multiplication
#  table of a user entered number.
# n=int(input("Enter the number"))
# table =[f"{n} X {i} = {n*i}"for i in range(1,11)]

# for line in table:
#         print(line)

# 4) Write a program to display a/b where a and b are integers.If b=0,display 
# infinite by handling the 'ZeroDivisionError'
# try:
#     a=int(input("Enter a : "))
#     b=int(input("Enter b : "))
#     print(a/b)
# except ZeroDivisionError as e:
#     print("Infinite")

# 5 Store the mutliplication tables generated in problem 3in afile named Tables.txt.
n =int(input("Enter a number: "))

table =[f"{n} X {i} = {n*i}" for i in range(1,11)]
with open("table.txt","a") as f:
    f.write(f"Table of {n} : {str(table)} \n")
    