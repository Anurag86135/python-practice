N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

if A == B:
    print("yes")
else:
    print("no")
