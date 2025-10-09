# a=23
# b=44
# c=99
# if a>b and a>c:
#     print("a is greater {} ".format(a))
# elif b>a and b>c:
#     print("b is greater",b)
# else:
#     print("c is greater",c)


# sum of digits of a number
# num =input("Enter the number :")

num=111
sum=0
count =0
while num>0:
    digit=num%10
    sum= sum +digit
    num=num//10
    count=count+1
print(sum)
print("count of digits",count)

# //prime numbers check
# num=24
# is_prime =True
# for i in range(2,num):
#     if num % i ==0:
#       is_prime=False
#       break
# if is_prime ==True:
#    print( num , "is prime number")
# else:
#    print(num, "is not prime number")

# //factorial of number
# n=5
# fact=1
# for i in range(1 ,n+1):
#  fact*=i
# print(fact)
