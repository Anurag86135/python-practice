n,r=map(int,input().split())
def factorial(x):
    result =1
    for i in range(1,x+1):
        result=result*i
    return result

nCr =factorial(n) // (factorial(r)*factorial(n-r))
nPr=factorial(n) //factorial(n-r)

print(nCr,nPr)