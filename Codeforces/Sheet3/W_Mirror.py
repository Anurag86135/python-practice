# Mirror Array

n,m=map(int,input().split())

matrix=[]
for _ in range(n):
    row =list(map(int,input().split()))
    matrix.append(row)

for i in matrix:
    i.reverse()
    print(*i)