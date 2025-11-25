# Check Code

a,b=map(int,input().split())
S=input()

#check length

if len(S)!=a+b+1:
    print("No")
    exit()

#check a-th index 
if S[a]!='-':
    print("No")
    exit()

# checking all the character
for i in range(len(S)):
    if i==a:
        continue
    if not S[i].isdigit():
        print("No")
        exit()
print("Yes")