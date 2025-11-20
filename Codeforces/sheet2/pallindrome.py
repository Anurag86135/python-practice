#pallindrome number

N= input()

rev=""
for ch in N:
    rev=ch+rev

rev=rev.strip('0')
if rev =='':
    rev='0'

print(rev)

if N==N[::-1]:
    print("YES")
else:
    print("NO")
