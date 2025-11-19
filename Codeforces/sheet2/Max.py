#maximum value
num=int(input())
arr=list(map(int,input().split()))

if len(arr)<num:
    print(f"please enter {num} values")
max=arr[0]
for i in range(1,len(arr)):
    if max<arr[i]:
        max=arr[i]

print(max)    