#Average 

def Average(num):
    
    total=0
    for i in num:
        total+=i
    
    print(total/len(num))


n=int(input())
num=list(map(float,input().split()))

Average(num)