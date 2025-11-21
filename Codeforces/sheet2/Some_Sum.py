# Some sums
N,a,b=map(int,input().split())


def digit_sum(x):
        return sum(map(int,str(x)))
        
total=0

for i in range(1,N+1):
        if a<=digit_sum(i)<=b:
            total+=i
print(total)
