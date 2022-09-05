from itertools import product

word = input()

splits = []

for i in range(2, len(word) + 1):
    pos = ""
    for j in range(7-i):
        pos += str(j+1)

    splits.append(list(product(pos, repeat=i)))

newsplits = []

for i in splits:
    for j in i:
        total = 0
        for k in j:
            total += int(k)

        if total == len(word):
            elements = []
            elements.append(0)
            sum = 0
            for k in j:
                sum += int(k)
                elements.append(sum)
            newsplits.append(elements)

del splits
count = 0
for i in newsplits:
    lst1 = []
    lst2 = []

    for j in range(len(i) - 1):
        lst1.append(word[i[j]:i[j+1]])

    for j in range(len(lst1)-1, -1, -1):
        lst2.append(lst1[j])

    if lst1 == lst2:
        count += 1
    
print(count)