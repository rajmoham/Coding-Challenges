dial1 = []
tempdial = []
dial2 = []

n, inp_txt = input().split(" ")
n = int(n)
ec_text = ""

for i in range(26):
    dial1.append(str(chr(i + 65)))
    tempdial.append(str(chr(i + 65)))

index = 0
for x in range(26):
    index += n

    if index > len(tempdial):
        while index > len(tempdial):
            index -= len(tempdial)

    dial2.append(tempdial[index - 1])
    del tempdial[index - 1]
    index -= 1

base_dial2 = 0

for i in inp_txt:
    ec_text += dial2[ord(i) - 65 + base_dial2]
    base_dial2 += 1
    if base_dial2 > len(dial2):
        base_dial2 -= len(dial2)

str_dial2 = ""
for i in range(6):
    str_dial2 += dial2[i]

print(str_dial2)
print(ec_text)
