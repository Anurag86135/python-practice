# # a=23
# # b=44
# # c=99
# # if a>b and a>c:
# #     print("a is greater {} ".format(a))
# # elif b>a and b>c:
# #     print("b is greater",b)
# # else:
# #     print("c is greater",c)


# # sum of digits of a number
# # num =input("Enter the number :")

num=434
digit =0
sum=0
count =0
while num>0:
 if(num%2==0):
      sum= sum +digit
      num=num//10
      count=count+1
print(sum)
print("count of digits",count)

# # //prime numbers check
# # num=24
# # is_prime =True
# # for i in range(2,num):
# #     if num % i ==0:
# #       is_prime=False
# #       break
# # if is_prime ==True:
# #    print( num , "is prime number")
# # else:
# #    print(num, "is not prime number")

# # //factorial of number
# # n=5
# # fact=1
# # for i in range(1 ,n+1):
# #  fact*=i
# # print(fact)
# # write program to display all prime numbers within a interval

# # for num in range(1,20):
# #   if num>1:
# #      for i in range(2,num):
# #         if (num%i)==0:
# #            break
# #      else:
# #         print(num) 
# # write a program to find the sum of all the prime numbers within a interval
# # sum=0 
# # for num in range(1,20):
# #   if num>1:
# #      for i in range(2,num):
# #         if (num%i)==0:
# #            break
# #      else:
# #         sum=sum+num
# #         print(sum)

# text = "madam"
# is_pallindrome = True
# for i in range (len(text)//2):
#     if text [i] != text[-(i+1)]:
#         is_pallindrome =False
#         break
# if is_pallindrome:
#     print(f"'{text}' is a pallindrome")
# else:
#     print(f"'{text}' is not a pallindrome")     


#     # num= 153
# # power =len(str(num))
# # total =0
# # for digits in str(num):
# #     total+=int(digits)**power
# # print(num,"is armstrong ?",total==num)