# Function for swapping two numbers
def Swap():
    a,b=map(int,input().split())
    temp=a
    a=b
    b=temp
    print(f"{a} {b}")

Swap()