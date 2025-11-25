# Minimize Number

n=int(input())

arr=list(map(int,input().split()))
count=0

while True:
    for x in range(len(arr)):
        if arr[x]%2==1:
            print(count)
            exit()

    for i in range(len(arr)):
        arr[i]=arr[i]//2
    count+=1
print(arr)