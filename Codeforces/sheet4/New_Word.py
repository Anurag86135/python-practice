#New Words

s=input().lower()

freq={}
for ch in s:
    freq[ch]=freq.get(ch, 0)+1


target ="egypt"
answer=0
#trying to form  "egypt" again and again
while True:
    possible=True

    #check that if all letters needed to form "egypt" exist
    for ch in target:
        if freq.get(ch,0)==0:
            possible=False
            break
    
    #if not possible,stop
    if not possible:
        break

    #if possible consume letters(use them)
    for ch in target:
        freq[ch]-=1

    #One word formed
    answer+=1

print(answer)