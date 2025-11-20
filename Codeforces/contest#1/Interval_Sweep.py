#Interval Sweep

a,b=map(int,input().split())

n=a+b

if n==0:
    print("NO")
elif n%2==0:
    print("YES" if a==b else "NO")#even length-> odd and even must be equal
else:
    print("YES" if abs(a-b)==1 else "NO")#odd length->counts differ by exactly
