# Z.Binary Search

def binary_search(arr,x):
    l,r=0,len(arr)-1
    while l<=r:
        mid =(l+r)//2
        if arr[mid] ==x:
            return True
        elif arr[mid]<x:
            l=mid+1
        else:
            r=mid-1
    return False

a,b=map(int,input().split())
num=list(map(int,input().split()))
num.sort()

for _ in range(b):
    x=int(input())
    if binary_search(num,x):
        print("found")
    else:
        print("not found")

                                
                
                                