# Divisor

def Divisor(num):
    total=0
    divisors =[]

    for i in range(1,num+1):
        if num%i==0:
            divisors.append(i)
    for i in divisors:
        total+=i
    
    print(total)


num=int(input())
Divisor(num)