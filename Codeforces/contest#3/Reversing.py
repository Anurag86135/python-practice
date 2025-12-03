#Reversing

n=int(input())
num=list(map(int,input().split()))

for i in range(n):
    if num[i]==0:
        num[:i]=reversed(num[:i])
print(*num)