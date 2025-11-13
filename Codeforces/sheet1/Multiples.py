a,b=map(int,input().split())

if(a%b==0):
    print("Multiples")
elif(b%a==0):
    print("Multiples")
else:
    print("No Multiples")