key1 = input()
key2 = input()

alphabet1 = []
alphabet2 = []

for i in range(26):
    if i != 16:
        alphabet1.append(chr(i + 65))
        alphabet2.append(chr(i + 65))

grid1 = []
grid2 = []

lst = []
for i in range(25 + len(key1)):
    if i < len(key1):
        if key1[i] not in lst:
            lst.append(key1[i])
    else:
        if alphabet1[i - len(key1)] not in lst:
            lst.append(alphabet1[i - len(key1)])
for i in range(5):
    row = []
    for j in range(5):
        row.append(lst[i*5 + j])
    grid1.append(row)
del lst

lst = []
for i in range(25 + len(key2)):
    if i < len(key2):
        if key2[i] not in lst:
            lst.append(key2[i])
    else:
        if alphabet2[i - len(key2)] not in lst:
            lst.append(alphabet2[i - len(key2)])

for i in range(5):
    row = []
    for j in range(5):
        row.append(lst[24 - (i*5 + j)])
    grid2.append(row)
del lst

print ("")
for i in range(5):
    print(" ".join(grid1[i]), "     ", " ". join(grid2[i]))
print("")

def Encryption(plaintxt):
    cyphertxt = ""
    if len(plaintxt)%2 == 1:
        plaintxt += "X"
    lst = []
    for i in range(0, len(plaintxt), 2):
        lst.append(plaintxt[i] + plaintxt[i+1])

    for pair in lst:
        for i in range(5):
            for j in range(5):
                if pair[0] == grid1[i][j]:
                    col1 = j 
                    row1 = i 
                    break
        for i in range(5):
            for j in range(5):
                if pair[1] == grid2[i][j]:
                    col2 = j
                    row2 = i
                    break
        if row1 == row2:
            if col1 == 4:
                cyphertxt += grid1[row1][0] 
            else:
                cyphertxt += grid1[row1][col1 + 1]
            if col2 == 4:
                cyphertxt += grid2[row2][0]
            else:
                cyphertxt += grid2[row2][col2 + 1]
        else:
            cyphertxt += grid1[row2][col1] 
            cyphertxt += grid2[row1][col2]

    print (cyphertxt)

def Decryption(cyphertxt):
    plaintxt = ""

    lst = []
    for i in range(0, len(cyphertxt), 2):
        lst.append(cyphertxt[i] + cyphertxt[i+1])
    for pair in lst:
        for i in range(5):
            for j in range(5):
                if pair[0] == grid1[i][j]:
                    col1 = j 
                    row1 = i 
                    break
        for i in range (5):
            for j in range (5):
                if pair[1] == grid2[i][j]:
                    col2 = j 
                    row2 = i 
                    break
        if row1 == row2:
            if row1 == 0:
                plaintxt += grid1[row1][4]
            else:
                plaintxt += grid1[row1][col1 - 1]
            if row2 == 0:
                plaintxt += grid2[row2][4]
            else:
                plaintxt += grid2[row2][col2 - 1]
        else:
            plaintxt += grid1[row2][col1] 
            plaintxt += grid2[row1][col2]
    
    if plaintxt[len(plaintxt) - 1] == "X":
        plaintxt = plaintxt[:len(plaintxt) - 1]
    print(plaintxt)

while True:
    command = input()
    if command == "Q":
        break
    elif command == "E":
        Encryption(input())
    elif command == "D":
        Decryption (input())
    print("")
