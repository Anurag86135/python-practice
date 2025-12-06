#Sort String

n=int(input())
s=input().strip()

freq=[0]*26
for ch in s:
    freq[ord(ch)-ord('a')]+=1
result=""

for i in range(26):
    result+=chr(i+ord('a'))*freq[i]

print(result)