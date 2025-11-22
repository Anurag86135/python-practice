# Lowest Number

N=int(input())

arr=list(map(int,input().split()))
lowest=arr[0]
idx=0
for i in  range(len(arr)):
    if arr[i]<lowest:
        lowest=arr[i]
        idx=i
        
print(f'{lowest} {idx+1}')

