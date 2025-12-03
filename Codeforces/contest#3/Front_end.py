# Front-End

n=int(input())
num=list(map(int,input().split()))

i,j=0,n-1

result=[]

while i<=j:
    result.append(num[i])
    i+=1
    if i<=j:
        result.append(num[j])
        j-=1
print(*result)