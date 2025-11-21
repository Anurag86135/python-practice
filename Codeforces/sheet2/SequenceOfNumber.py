# Sequence of a numbers and sum
while True:
    a,b=map(int,input().split())
    total=0
    low=min(a,b)
    high=max(a,b)


    if low<=0 or high<=0:       
       break
    else:
        for i in range(low,high+1):
            print(i,end=' ')
            total+=i
        print(f"sum ={total}")
        
