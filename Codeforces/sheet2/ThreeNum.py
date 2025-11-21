# Three Numbers

K,S =map(int,input().split())
count=0
for X in range(0,K+1):
    low=max(0,S-X-K)
    high=min(K,S-X)

    if low<=high:
        count +=(high -low +1)
        
print(count)