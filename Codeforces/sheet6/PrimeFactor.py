# prime Factor


n=int(input())
temp=n
factors=[]

i=2
while i*i<=n:
    if n%i==0:
        count=0
        while n%i==0:
            n//=i
            count+=1
        factors.append((i,count))
    i+=1
if n>1:
    factors.append((n,1))

result =[]
for p,c in factors:
    result.append(f"({p}^{c})")
print("*".join(result))
