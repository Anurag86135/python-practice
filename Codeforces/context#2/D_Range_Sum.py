# Range Sum

T=int(input())

for i in range(T):
    L,R=map(int,input().split())
    if(L>R):
        L,R=R,L
    sum_R=R*(R+1)//2 # adding no. from 1 to R

    sum_L=L*(L-1)//2# adding number from 1 to l-1
    print(sum_R-sum_L)