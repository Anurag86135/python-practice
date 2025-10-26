import math
t = int(input())
for _ in range(t):
    nums = list(map(int, input().split()))
    x = nums[0]
    y = nums[1]
    
    gcd = math.gcd(x, y)
    lcm = (x * y) // gcd
    print(gcd, lcm)
