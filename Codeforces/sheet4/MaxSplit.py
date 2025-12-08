# Max Split

s=input().strip()

countL=0
countR=0
current=""
parts=[]

for ch in s:
    current+=ch 
    if ch =='L':
        countL+=1
    else:
        countR+=1
    
    if countL ==countR:
        parts.append(current)
        current="" 
        countL=countR=0
print(len(parts))
for p in parts:
    print(p)