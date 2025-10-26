n = int(input())   # number of works

for _ in range(n):
    sh, sm, eh, em = map(int, input().split())

    
    hour = eh - sh # calculate hour and minute difference
    minute = em - sm

    # if minute are negative borrow 1 hour = 60 minutes
    if minute < 0:
        minute += 60
        hour -= 1

    print(hour, minute)
