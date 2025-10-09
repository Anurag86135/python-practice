#Question 3. Write a program in python to print the contents of a directory using os module.
# Seach online for the funtion which does that/?

import os 
#Specify the directory you want to list
directory_path="/"

#List all files and directories in the specified path
contents=os.listdir(directory_path)

#print each file and directory Name
# for item in contents:
#         print(item)


'''Or we can also print like this the  contents of the directory'''
print(contents)