row = list(input())

def ReturnMissing(left, right):
    lst = ["R", "G", "B"]

    for i in range(len(lst)):
        if lst[i] == left:
            del lst[i]
            break
    for i in range(len(lst)):
        if lst[i] == right:
            del lst[i]
            break

    return lst[0]


for i in range(len(row) - 1):
    nextrow = ""
    for j in range(len(row) - 1):
        if row[j] == row[j + 1]:
            nextrow += row [j]
        else:
            nextrow += ReturnMissing(row[j], row[j+1])
    row = list(nextrow)

print(row[0])