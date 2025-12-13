# MaxMin

def Max(arr,n) :
   Max =arr[0]
   for i in range(n):
      if(arr[i]>Max):
         Max=arr[i]
 
   return Max


def Min(arr,n):
   Minimum=arr[0]
   for i in range(n):
      if(arr[i]<Minimum):
         Minimum=arr[i]

   return Minimum


n=int(input())
arr=list(map(int,input().split()))
minim=Min(arr,n)
Maxim=Max(arr,n)
print(f"{minim} {Maxim}")



         


