# h.N.Times
def Times(a,b):
    for i in range(a):
        print(b,end=" ")
    print()

    

n=int(input())
for i in range(n):
    a,b=input().split()
    a=int(a)
    Times(a,b)

