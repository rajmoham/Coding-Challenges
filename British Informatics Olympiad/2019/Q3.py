from itertools import permutations

num, start = input().split(" ")
num = int(num)

blocks = []

for i in range(num):
    blocks.append(chr(i + 65))

for i in start:
    for j in range(len(blocks) - 1, -1, -1):
        if i == blocks[j]:
            del blocks[j]

blocks = "".join(blocks)
block_chains = []
for i in list(permutations(blocks, num - len(start))):
    block_chains.append(start+("".join(i)))

count = 0

for i in block_chains:
    alphabetical = False
    for d1 in range(len(i) - 2):
        for d2 in range(d1 + 1, len(i) - 1):
            for d3 in range(d2 + 1, len(i)):
                if ord(i[d2]) == ord(i[d1]) + 1 and ord(i[d3]) == ord(i[d2]) + 1:
                    alphabetical = True
                    break
            if alphabetical == True:
                break
        if alphabetical == True:
            break
    if alphabetical == False:
        count += 1

print(count)