# Digits

n=int(input())

for _ in range(n):
    n=input().strip()
    digits=list(n)
    digits.reverse()
    print(" ".join(digits))