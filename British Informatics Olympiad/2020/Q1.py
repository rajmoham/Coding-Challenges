'''r_string, n = input().split(" ")
n = int(n)

def NumeralCount(num):
    numerals = {10:"X", 9:"IX", 5:"V", 4:"IV", 1:"I"}
    n_string = ""
    while num != 0:
        for i in numerals:
            if num >= i:
                num -= 1
                n_string += numerals[i]
                break
    return n_string

for i in range(n):
    roman = ""

    last_chr = ""
    counts = 0
    for i in r_string:
        if i == last_chr:
            counts += 1
        else:
            roman += NumeralCount(counts) + last_chr
            last_chr = i
            counts = 1
    roman += NumeralCount(counts) + last_chr

    r_string = roman

num_I = 0
num_V = 0
for i in r_string:
    if i == "I":
        num_I += 1
    if i == "V":
        num_V += 1

print(num_I, num_V)
print(r_string)'''

        
