# Counting Elements 
n=int(input())
arr=list(map(int,input().split()))
count=0
for i in arr:
    if i+1 in arr:
        count+=1
print(count)
