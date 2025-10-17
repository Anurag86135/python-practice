# 6)write a program to mine a log file and find out whether it contains 'python'.

# with open("log.txt") as f:
#     content =f.read()

# if("python" in content):
#     print("Yes python is present")
# else:
#     print("not present in this file")



#7) Write a program to find out the line number when python is present from question 6
# with open("log.txt") as f:
#     lines =f.readlines()

#     lineno=1

#     for line in lines:
#         if("python" in line):
#             print(f"Yes python is present. Line no: {lineno}")
#             break
#         lineno+=1
#     else:
#         print("Not present in that file")


#8) Write a program to make a copy of text file"log .txt"
# with open("log.txt") as f:
#     content=f.read()

# with open("log_copy.txt","w") as f:
#     f.write(content)


# 9)Writ a python program to rename a file "renamed _by_python.txt".

# with open("poem.txt") as f:
#     content=f.read()

# with open("renamed_by_python",'w') as f:
#     f.write(content)


# 10) Write a program to find out whether a file is 
# identical and matches the content of another file.

# with open("log.txt") as f:
#     content1=f.read()

# with open("log_copy.txt") as f:
#     content2=f.read()

# if (content1==content2) :
#     print("yes they both are identical")
# else:
#     print("not identical different")

# 11)Write a python program to wipe out the content of a file using python
with open("poem.txt","w") as f:
 content= f.write("")