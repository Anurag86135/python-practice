# Winter Sale
x,p = map(float, input().split())


if x >= 100:
    print("Invalid discount")
else:
    d = (100 * p) / (100 - x)
    print(f"{d:.2f}")