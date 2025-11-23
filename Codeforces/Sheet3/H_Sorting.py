# Sorting

N=int(input())

arr=list(map(int,input().split()))

for i in range(len(arr)):
   for j in range(0,len(arr)-1):
      if(arr[j]>arr[j+1]):
         temp=arr[j]
         arr[j]=arr[j+1]
         arr[j+1]=temp
         
print(*arr)
         