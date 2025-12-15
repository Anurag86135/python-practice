# Shift Right

def shift_right(arr,n,x):
    x=x%n # reduce extra shifts
    result= arr[-x:]+ arr[:-x]
    return result


n,x=map(int,input().split())
arr =list(map(int,input().split()))

# Function call
ans=shift_right(arr,n,x)

for i in ans:
    print(i, end=" ")
