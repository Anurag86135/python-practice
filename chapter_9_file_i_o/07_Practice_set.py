# 3)Write a program to generate multiplication tables from 2 to 20 and write it to the different files.
# Place these files in a folder for a 13-year old.

# def generateTable(n):
#     table=""
#     for i in range(1,11):
#         table+=f"{n} X {i} ={n*i}\n"
    
#     with open(f"tables/table_{n}.txt","w") as f:
#         f.write (table)


# for i in range(2,21):
#     (generateTable(i))


# -------------------------------------------

# # 4)A file contains a word "Donkey" multiple times. 
# # You need to write a program which replace this word with #### by updating the same file.

# word ="Donkey"

# with open("file.txt","r") as f:
#     content=f.read()

# contentNew =content.replace(word,"#####")

# with open("file.txt","w") as f:
#     f.write(contentNew)


# ---------------------------------------------

# 5) Repeat program 4 for a list of such words to be censored.

words=["Donkey" ,"is","guy","people"]

with open ("file.txt","r") as f:
    content=f.read()

for word in words:
    content=content.replace(word,"#" * len(word))

with open("file.txt","w") as f:
    f.write(content)


