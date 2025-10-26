# Input amount
amount = int(input("Enter the amount: "))

# Input available denomination
available_denomination = int(input("Enter the highest denomination present: "))

remaining = amount

denominations = [100, 50, 20, 10, 5, 2, 1]

for  i in denominations:
    if i <= available_denomination:
        note_count = 0
        match i:
            case 100:
                note_count = remaining // 100
                remaining = remaining % 100
                print(f"100 rupees note: {note_count}")
            case 50:
                note_count = remaining // 50
                remaining = remaining % 50
                print(f"50 rupees note: {note_count}")
            case 20:
                note_count = remaining // 20
                remaining = remaining % 20
                print(f"20 rupees note: {note_count}")
            case 10:
                note_count = remaining // 10
                remaining = remaining % 10
                print(f"10 rupees note: {note_count}")
            case 5:
                note_count = remaining // 5
                remaining = remaining % 5
                print(f"5 rupees note: {note_count}")
            case 2:
                note_count = remaining // 2
                remaining = remaining % 2
                print(f"2 rupees note: {note_count}")
            case 1:
                note_count = remaining
                remaining = 0
                print(f"1 rupees note: {note_count}")