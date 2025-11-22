# B_Searching

N=int(input())
arr=list(map(int,input().split()))
item=int(input())
found=False
for i in range(len(arr)):
    if arr[i]==item:
        print(i)
        found=True
        break
    
if found==False:
    print(-1)


