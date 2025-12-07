# Reverse words of the string

s=input()
rev=[]
words=s.split()

for w in words:
   rev.append(w[::-1])
print(" ".join(rev))