#Count Word
s = input()
count = 0
in_word = False

for ch in s:
    if ch.isalpha():         # letter mila
        if not in_word:
            count += 1
            in_word = True
    else:                     # non-letter mila -> word khatam
        in_word = False

print(count)

