# Alternating Array


n=int(input())
arr=list(map(int,input().split()))

countA=0
countB=0

for i,x in enumerate(arr):
    is_pos=x>0

    A_pos=(i%2==0)
    if is_pos!=A_pos:
        countA+=1

    B_pos=not A_pos
    if is_pos!=B_pos:
        countB+=1
print(min(countA,countB))