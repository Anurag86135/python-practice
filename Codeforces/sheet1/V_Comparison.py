n1,s,n2=input().split()

n1=int(n1)
n2=int(n2)

if s=="<":
    check= n1<n2
elif(s==">"):
    check=n1>n2
elif(s=="="):
    check=n1==n2

if check is True:
    print("Right")
else:
    print("Wrong")

