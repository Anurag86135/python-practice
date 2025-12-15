# Swapping with matrix

def swap_matrix(n,x,y,mat):
    x-=1
    y-=1
    
    #swap rows
    mat[x], mat[y] =mat[y] ,mat[x]
    #swap columns
    for i in range(n):
        mat[i][x],mat[i][y]=mat[i][y],mat[i][x]

    return mat
n,x,y =map(int,input().split())
matrix=[list(map(int,input().split()))for _ in range(n)]

#Function call
result=swap_matrix(n,x,y,matrix)

#output
for row in result:
    print(*row)