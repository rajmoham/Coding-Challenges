from itertools import product

morse_code = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..",
                ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", "...",
                "-", "..-", ".-.", "...-", ".--", "-..-", "-.--", "--.."]
msg = input()

morse_msg = ""
for i in msg:
    morse_msg += morse_code[ord(i) - 97]
    print(morse_msg)

lst_splits = list(product("1234", repeat=(len(msg))))
pos = []

for i in lst_splits:
    total = 0
    for j in i:
        total += int(j)
    if total == len(morse_msg):
        pos.append(i)

del lst_splits
count = 0

lst_pos = []
for i in pos:
    temp_lst = []
    temp_lst.append(0)
    for j in range(len(i)):
        total = 0
        for k in range(j+1):
            total += int(i[k])
        temp_lst.append(total)
    lst_pos.append(temp_lst)

for i in range(len(pos)):
    in_morse = True
    for j in range(len(msg)):
        if morse_msg[lst_pos[i][j]:lst_pos[i][j+1]] not in morse_code:
            in_morse = False
            break
    if in_morse == True:
        count += 1

print(count)