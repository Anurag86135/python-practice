# Lucky Array

N=int(input())

num=list(map(int,input().split()))

min=min(num)

freq=num.count(min)

if freq % 2 == 1 :
    print("Lucky")
else:
    print("Unlucky")
