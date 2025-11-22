# Replacement

N=int(input())

arr=list(map(int,input().split()))

for i in arr:
   if i<0:
      print(2,end=" ")
   elif(i==0):
      print(0,end=" ")
   else:
      print(1,end=' ')