letter1, letter2, n = input().split(" ")
sequence = []

letter1 = ord(letter1) - 64
sequence.append(letter1)
letter2 = ord(letter2) - 64
sequence.append(letter2)
n = int(n)

for i in range(1, n - 1):
    next = sequence[i] + sequence[i - 1]
    if next > 26:
        next -= 26

    sequence.append(next)

letter = chr(sequence[len(sequence) - 1] + 64)
print(letter)