# Good or Bad

t=int(input())

for _ in range(t):
    n=input()

    if '010' in n or '101' in n:
        print("Good")
    else:
        print("Bad")