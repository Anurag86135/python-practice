# Sum of Consecutive Odd Numbers

n=(int(input()))


for _ in range(n):
    a,b=map(int,input().split())
    if a>b:
        a,b=b,a

    total=0
    
    for i in range(a+1,b):
        if i%2!=0:
            total+=i

    print(total)