# # # 1)Write a program to print multiplication table of a given number using for Loop 

# # n=int(input('enter the number for printing its table '))
# # for i in range(1,11):
# #     # print(n," X ", i," = " ,n*i)
# #     print(f"{n} X {i}={n*i}")

# # 2) Write a program to greet all the person names stored in a list 'l' and which starts with 's'.
# l=["harry","Sohan","sachin","rahul","Anurag","sahrukh"]

# for name in l:
#     if(name.startswith("S")):
#         print(f"Hello {name}")



# Write your first program with while loop instead of for loop
n= int(input("Enter a number"))
i=1
while(i<11):
    print(f"{n} X {i} = {n*i}")
    i=i+1