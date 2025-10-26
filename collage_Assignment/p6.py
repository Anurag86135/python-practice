def reverse_number(num):
    return int(str(num)[::-1])

n = int(input("Enter number of test cases: "))

for _ in range(n):
    a, b = input("Enter two numbers: ").strip().split()
    a = int(a)
    b = int(b)

    a_rev = reverse_number(a)
    b_rev = reverse_number(b)

    total = a_rev + b_rev
    result = reverse_number(total)

    print(result)
