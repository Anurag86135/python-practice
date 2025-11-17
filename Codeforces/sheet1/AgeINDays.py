# Age in Days
N=int(input())

years=N//365
remaining=N%365
months=remaining//30
days =remaining%30

print(f"{years } years")
print(f"{months } months")
print(f"{days } days")
