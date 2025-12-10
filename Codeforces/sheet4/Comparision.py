# Comparision 

S=input().strip()

smallest_string=S

for i in range(1,len(S)):
    x=S[:i]
    Y=S[i:]
    new_string =''.join(sorted(x))+''.join(sorted(Y))
    if new_string<smallest_string:
        smallest_string=new_string

print(smallest_string)