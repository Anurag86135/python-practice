#5) write a python function to print  first n lines  of the following pattern:
'''   ***
      **
      *       '''
# def Pattern(n):
#     if(n==0):
#         return 
#     print("*"*n)
#     Pattern(n-1)# recursion

# Pattern(4)


# 6) Write a python function which converts inches to cms.

# def inch_to_cm(inch):
#     return inch *2.54

# n=int(input("Enter value in inches"))

# print(f"The Corresponding value in cms is{ inch_to_cm(n)}")

#7) Write a python function to remove a given word from a list ad strip at the same time.

# def remove(l,word):
#     n=[]
#     for item in l:
#         if not(item==word):
#             n.append(item.strip(word))
#     return n
# l=["Harry","Rohan","Shubham","an"]

# print(remove(l,"am"))



# 8) write a python function to print multiplication table of a given number
def table(n):
    for i in range(1,11):
        print(f"{n} X { i} = {i*n}")

print(table(6))