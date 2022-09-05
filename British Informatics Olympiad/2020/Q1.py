r_string, n = input().split(" ")
n = int(n)

numerals = {10:"X", 9:"IX", 5:"V", 4:"IV", 1:"I"}

def NumeralCount(string):
    last_char = string[0]
    num = 0
    chars = []
    counts = []
    for i in string:
        if last_char == i:
            num += 1
        else:
            chars.append(last_char)
            counts.append(num)
            last_char = i
            num = 1
    chars.append(last_char)
    counts.append(num)

    return chars, counts

def GetNewString(character, char_count):
    new_string = ""
    for i in range(len(character)):
        num = char_count[i]
        while num != 0:
            for j in numerals:
                if num >= j:
                    num -= j
                    new_string += numerals[j]
                    break
        new_string += character[i]

    return new_string    

for i in range(n):
    character, char_count = NumeralCount(r_string)
    r_string = GetNewString(character, char_count)

num_I = 0
num_V = 0
for i in r_string:
    if i == "I":
        num_I += 1
    if i == "V":
        num_V += 1

print(num_I, num_V)

        
