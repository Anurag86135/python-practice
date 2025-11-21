# Number Histogram

s=input()
n=int(input())
arr=list(map(int,input().split()))


if(n!=len(arr)):
    print("out of bound")
else:
    for i in arr:
        print(s*i)