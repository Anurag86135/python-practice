# Divisor

def Divisor(num):
    total=0
    divisors =[]

    for i in range(1,int(num**0.5)+1):
        if num%i==0:
            total+=i
            if i!=num//i:
                total+=num//i
    
    print(total)


num=int(input())
Divisor(num)