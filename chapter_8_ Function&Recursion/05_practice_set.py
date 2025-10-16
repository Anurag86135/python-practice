# # 1)  WRITE A PROGRAM USING FUNCTION TO FIND GREATEST OF THREE NUMBERS
# def greatest(a,b,c):
#     if(a>b and a>c):
#         return a
#     if(b>a and b>c):
#         return b
#     if(c>a and c>b):
#         return c
    
# a=22
# b=33
# c=90

# print(greatest(a,b,c))
  

# Write  a python program using function to convert Celcius to fahrenheit.
#  formula for it --> c=5*(f-32)/9

# def f_to_c(f):
#     return 5*(f-32)/9

# f=int(input("Enter temperature in F : "))
# c=f_to_c(f)
# print(f"{round(c,1)} ° C ")

#3) how do you prevent  a python print() function to print new line at the end

# Answer-> with the help of end=""


# print("Anurag")
# print("ji")
# print("GOOD", end="")
# print("Boy" end="")


# 4) Write a recursive function to calculate the sum of  first n natural number:
''' sum(n)= 1+2+3+..+n
means,
sum(1)=1
sum(2)=1+2
sum(3)=1+2+3


SUM(N)=1+2+3+4....+N

sum(n) = sum(n-1)+n'''
n=5
def SUM(n): 
    if(n==1):
        return 1
    return SUM(n-1)+n

print(SUM(n))