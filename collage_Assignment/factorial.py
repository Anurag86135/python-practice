# def factorial(n):
#     if(n==0 or n==1):
#         return 1
#     return n* factorial(n-1)

# n=int(input("Enter the number"))
# print(f"factorial  of {n} is :{factorial(n)}")


# def febo(num):

#     if(num<=1):
#         return num
#     return febo(num-1) +febo(num-2)
# nthterm=int(input("Enter value of n"))
# for num in range(nthterm):
#     print(febo(num))


#sum of n natural number
# def sum(num):
#     if num ==1:
#         return 1
#     else:
#      return  num+sum(num-1)
    
# num=int(input("Enter num : "))
# print(sum(num))

# n=5
# sum=0
# for i in range(1,n+1):
#       sum+=i
# print(sum)

# print 1 to 5
# def mul(n):
#     if n==0:
#         return
#     mul(n-1)
#     print(n ,end=" ")
    
    
# n=5
# mul(n)

# #  print 5 to 1
# def mul(n):
#     if n==0:
#         return
   
#     print(n ,end=" ")
    
#     mul(n-1)
    
    
# n=5
# mul(n)

# even upto n
# def even(n):
#     if n==0:
#         return
#     even(n-1)
#     if(n%2==0):
#       print(n, end=" ")

# n=10
# even(n)

#  sum of n digit

# def sum(n):
#     if(n==0):
#         return 0
#     return (n%10) + sum(n//10)
# n=12345
# print(sum(n))

# lamda function

# Add =lambda x,y:x+y

# print(Add(2,4))

# sum of digit 

# num=int(input("enter the number: "))

# sumof_digit=lambda num: 0 if num==0 else num%10+ sumof_digit(num//10)
# print(sumof_digit(num)

# from normal way instead of recursion

# from functools import reduce

# num =12345
# digits =list(map(int,str(num)))

# sum_of_digits =reduce(lambda x,y:x+y,digits)

# print(sum_of_digits)

# date-02/11/2025

#paalindrome number

word=int(input("Enter the word :"))
word=str(word)
is_pallindrome = False

for i in range(len(word)//2):
    if word[i]==word[len(word)-1-i]:
        is_pallindrome = True
        break
    
if is_pallindrome:
    print("Pallindrome hai")
else:
    print("nahi hai pallindrome")








