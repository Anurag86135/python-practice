# O. Fibonacci

N=int(input())

if N==1:
    print(0)
    exit()

if N==2:
    print(1)
    exit()

a=0 # it is fib(1)
b=1 # it is fib(2)

for i in range(3,N+1):
    c=a+b
    a=b
    b=c
print(c)