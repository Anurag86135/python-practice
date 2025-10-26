#  number of people
n = int(input())

# Input  minimum skill required
x = int(input())

# Loop through each person's skill
for i in range(n):
    z = int(input())   # skill of ith person
    if z >= x:
        print("YES")
    else:
        print("NO")
