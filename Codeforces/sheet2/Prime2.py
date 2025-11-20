# prime numbers from 1 to N

N=int(input())

for num in range(2,N+1):
    is_prime =True

    for i in range(2,num):
        if num%i==0:
            is_prime=False
            break

    if is_prime:
        print(num,end=" ")
 