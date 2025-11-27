# Q.Count Subarrays

t=int(input())

for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))

    count=1
    chain=1

    for i in range(1,n):
        if arr[i]>=arr[i-1]:
            chain+=1
        else:
            chain=1

        count+=chain

    print(count)