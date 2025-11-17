# Z. Hard Compare

import math


n1,n2,n3,n4=map(int,input().split())

if (n2*math.log(n1)>n4*math.log(n3)):
    print("YES")
else:
    print("NO")