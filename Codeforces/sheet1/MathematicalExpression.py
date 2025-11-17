# W.Mathematical Expression

n1,s1,n2,s2,n3=input().split()

n1=int(n1)
n2=int(n2)
n3=int(n3)

if s1 == "+":
    check=n1+n2
elif s1=="-":
    check=n1-n2
elif s1=="*":
    check=n1*n2
elif(s1=="/"):
    check=n1/n2

if check ==n3 :
    print("Yes")
else:
    print(check)
