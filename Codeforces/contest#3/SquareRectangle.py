# Square and Rectangle

n=int(input())

for i in range(n):
    num=list(map(int,input().split()))

    if num[0]==num[1]:
        print("Square")
    else:
        print("Rectangle")