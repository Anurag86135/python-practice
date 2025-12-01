# U . Is B a subsequence of A ?



n,m=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

i=0
j=0

while i<n and j<m:
    if A[i]==B[j]:
        j+=1
    i+=1

if j==m:
    print("YES")
else:
    print("NO")
