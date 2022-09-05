from itertools import combinations, product
from timeit import repeat

p, q, r = input().split(" ")
p, q, r = int(p), int(q), int(r)
n = int(input())

letters = ""
for i in range(p):
    letters += chr(i + 65)

combinations = list(product(letters, repeat=r))

count = 0

for i in combinations:
    last_chr = ""
    repeats = 1
    for j in i:
        if j != last_chr:
            last_chr = j
            repeats = 1
        else:
            repeats += 1
        if repeats > q:
            break
    if repeats <= q:
        count += 1

    if count == n:
        print("".join(i))
        break