number = int(input())
numlist = list(str(number))

output = ""

for i in range(2, 10):
    anagram = False

    new_num = number * i
    new_numlist = list(str(new_num))

    numlist.sort()
    new_numlist.sort()

    for j in range(len(numlist)):
        if numlist[j] != new_numlist[j]:
            anagram = False
            break
        else:
            anagram = True
    if anagram == True:
        output += str(i) + " "

if output == "":
    print("NO")
else:
    print(output)