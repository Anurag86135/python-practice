n = int(input())

round = 1

while True:
    # Ramesh ki turn
    if n <= round:
        print("Ramesh")
        break
    n -= round

    # Suresh ki turn
    if n <= round * 2:
        print("Suresh")
        break
    n -= round * 2

    round += 1
