# V _ FrequencyArray


n,m=map(int,input().split())

A=list(map(int,input().split()))


freq=[0]*(m+1)

for x in A:
    freq[x]+=1

for i in range(1,m+1):
    print(freq[i])



