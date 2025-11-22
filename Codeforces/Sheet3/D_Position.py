#   Positions in array

N=int(input())

arr=list(map(int,input().split()))

for i in range(len(arr)):
    if arr[i]<=10:
        print(f"A{[i]} = {arr[i]} ")

