#New Array
def Array(a,b):
    c=b+a
    return c

n=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

#function call

C=Array(A,B)

for i in C:
    print(i,end=" ")

 

    
