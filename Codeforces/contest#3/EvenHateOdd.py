# Even Hate Odd

n=int(input())

for _ in range(n):
    num=int(input())
    l=list(map(int,input().split()))

    if num%2!=0:
        print(-1)
        continue

    count_even =sum(1 for x in l if x%2 ==0)
    required =num//2
    print(abs(count_even - required))