# Five in one

def get_max(arr):
    return max(arr)

def get_min(arr):
    return min(arr)

def is_prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def count_primes(arr):
    count=0
    for x in arr:
        if is_prime(x):
             count+=1
    return count

def is_palindrome(n):
    s=str(n)
    return s==s[::-1]

def count_palindromes(arr):
    count=0
    for x in arr:
        if is_palindrome(x):
            count+=1
    return count


def count_divisors(n):
    cnt=0
    for i in range(1,n+1):
        if n%i ==0:
            cnt+=1
    return cnt

def max_divisiors_number(arr):
    max_div=0
    ans=arr[0]

    for x in arr:
        d=count_divisors(x)
        if d> max_div or (d ==max_div and x>ans):
            max_div=d
            ans=x
    return ans
        
n=int(input())
arr=list(map(int,input().split()))

print(f"The maximum number : {get_max(arr)}")
print(f"The minimum number : {get_min(arr)}")
print(f"The number of prime numbers : {count_primes(arr)}")
print(f"The number of palindrome numbers : {count_palindromes(arr)}")
print(f"The number that has the maximum number of divisors : {max_divisiors_number(arr)}")