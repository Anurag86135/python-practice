#factorial

num=int(input())

for i in range(num):
    N=int(input())

    fact=1

    for i in range(1,N+1):
        fact*=i

    print(fact)