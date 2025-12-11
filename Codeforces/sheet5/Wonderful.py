# Wonderful number

def is_binary_pallindrome(n):
    b=bin(n)[2:]
    return b==b[::-1]

def is_wonderful(n):
    if n%2==0:
        return False
    return is_binary_pallindrome(n)

n=int(input())
print("YES" if is_wonderful(n) else "NO")