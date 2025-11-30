# Construct the Sum

t=int(input())

for _ in range(t):
    n,s=map(int,input().split())
    remaining=s
    ans=[]

    for x in range(n,0,-1):
        if x<=remaining:
            ans.append(x)
            remaining-=x
    if remaining==0:
        print(*ans)
    else:
        print(-1)