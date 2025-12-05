# I Love Strings
t=int(input())

for _ in range(t):
    s,m=input().split()

    result=""

    min_len=min(len(s),len(m))

    for i in range(min_len):
        result+=s[i] +m[i]

    result+=s[min_len:]+m[min_len:]

    print(result)