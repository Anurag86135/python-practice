# Search In Matrix

n,m=map(int,input().split())
matrix=[]
check=False

for i in range(n):
     row=list(map(int,input().split()))
     matrix.append(row)
x=int(input())

for i in range(n):
     for j in range(m):
          if matrix[i][j]==x:
               check=True
               break
          
if check:
     print("will not take number")
else:
     print("will take number")          
               