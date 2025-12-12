#Equation

def Equation():
    a,b=map(int,input().split())

    s=0

    for power in range(2,b+1,2):
        value =1
        for i in range(power):
            value*=a
        s+=value
    print(s)


Equation()