# M_Replace MinMax

t=int(input())

arr=list(map(int,input().split()))

minArr=min(arr)
maxArr=max(arr)

for i in range(len(arr)):
    if arr[i] ==minArr:
        arr[i]=maxArr
    
    elif (arr[i]== maxArr):
         arr[i] =minArr


print(*arr)