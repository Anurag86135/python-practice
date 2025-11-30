# Break Number

n=int(input())
arr=list(map(int,input().split()))

m=0

for i in arr:
    count=0
    while i%2==0:
        count+=1
        i//=2

        m=max(m,count)

print(m)