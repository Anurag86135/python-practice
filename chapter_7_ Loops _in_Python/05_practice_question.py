#9 write a program to print  this pattern
'''***
   * *
   *** '''
# n= int(input("ENter the number :"))
# for i in range(1,n+1):
#     if(i==1 or i==n):
#         print("*" *n, end="")
#     else:
#         print("*", end ="")
#         print(" "*(n-2),end ="")
#         print("*", end="")
#     print("")

# 10) write a program to print multiplication table of n using  for loops in reversed order.
n=int(input("Enter the number :"))
for i in range(1,11):
  print(f"{n} X {11-i}={n*(11-i)}")
