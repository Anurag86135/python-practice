# Two numbers with floor ,ceil and Round
import math
a,b=input().split()

a=int(a)
b=int(b)

print(f"floor {a} / {b} = {math.floor(a/b)}")
print(f"ceil {a} / {b} = {math.ceil(a/b)}")
print(f"round {a} / {b} = {round(a/b+0.5)}")