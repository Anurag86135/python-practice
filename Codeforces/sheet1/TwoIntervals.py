# Two intervals
l1,r1,l2,r2=map(int,input().split())

left=max(l1,l2)
right=min(r1,r2)

if left <= right:
    print(left,right)
else:
    print(-1)