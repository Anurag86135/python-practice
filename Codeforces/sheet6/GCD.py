#GCD

def gCD(a,b):
    while b!=0:
        a,b=b,a%b
    return a

A,B=map(int,input().split())
G=gCD(A,B)
L=(A//G)*B

print(G,L)