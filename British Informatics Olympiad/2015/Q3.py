from itertools import permutations
from math import perm

a, b, c, d, n = input().split(" ")
a, b, c, d, n = int(a), int(b), int(c), int(d), int(n)

sum = a + b + c + d

works = ""

for i in range(a):
    works += "A"
for i in range(b):
    works += "B"
for i in range(c):
    works += "C"
for i in range(d):
    works += "D"

pos = list(permutations(works, sum))
exhibition = []
count = 0
for i in pos:
    if i not in exhibition:
        exhibition.append(i)
        count += 1

    if count == n:
        break

print("".join(exhibition[len(exhibition) - 1 ]))