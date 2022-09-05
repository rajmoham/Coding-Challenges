from unicodedata import digit


digits = ("ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE")
word = input()

output = ""

for i in range(len(digits)):
    j = 0
    k = 0

    while j < len(digits[i]) and output == "":
        while k < len(word):
            if word[k] == digits[i][j]:
                j += 1
                if j == len(digits[i]):
                    output = str(i + 1)
                    break
            k += 1

        if (j < len(digits[i])):
            break

if output == "":
    print("NO")
else:
    print(output)