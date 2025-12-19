# Sum of Range

def sum_all(n):
    return n * (n + 1) // 2

def sum_even(n):
    k = n // 2
    return k * (k + 1)

def sum_odd(n):
    k = (n + 1) // 2
    return k * k

A, B = map(int, input().split())

L = min(A, B)
R = max(A, B)

print(sum_all(R) - sum_all(L - 1))
print(sum_even(R) - sum_even(L - 1))
print(sum_odd(R) - (L // 2) ** 2)
