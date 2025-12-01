# Matrix

n=int(input())
matrix=[]
for i in range(n):
    row =list(map(int,input().split()))
    matrix.append(row)

main_diag =[]
sec_diag =[]

for i in range(n):
    main_diag.append(matrix[i][i])
    sec_diag.append(matrix[i][n-1-i])
total=sum(main_diag)-sum(sec_diag)

print(abs(total))
