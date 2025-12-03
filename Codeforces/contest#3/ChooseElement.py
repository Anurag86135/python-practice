#choose Element

n,k=map(int,input().split())
num=list(map(int,input().split()))

num.sort(reverse=True)
total=0
for i in range(k):
    if num[i]>0:
        total+=num[i]
    else:
        break
print(total)



