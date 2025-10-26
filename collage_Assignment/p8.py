# Function to find last digit of a^b
def last_digit(a, b):
    cycle = []
    current = a % 10
    while current not in cycle:
        cycle.append(current)
        current = (current * a) % 10
    
    # Determine position in cycle
    index = (b % len(cycle)) - 1  # -1 because list is 0-indexed
    return cycle[index]

# Input number of test cases
N = int(input("Enter test cases how many time you want to run the program : "))

for _ in range(N):
    a, b = map(int, input().split())
    print(last_digit(a, b))