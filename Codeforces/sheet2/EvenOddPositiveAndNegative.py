num=int(input())
arr =list(map(int,input().split()))

if len(arr)!=num:
    print("You must enter exactly" , num, "numbers.")
    exit()


Even=0
Odd=0
Positive=0
Negative=0



for num in arr:
    if num%2==0:
        Even+=1
    else:
        Odd+=1

    if num>0:
        Positive+=1
    elif (num<0):
        Negative+=1
        

print(f"Even: {Even}")
print(f"Odd: {Odd}")
print(f"Positive: {Positive}")
print(f"Negative: {Negative}")




