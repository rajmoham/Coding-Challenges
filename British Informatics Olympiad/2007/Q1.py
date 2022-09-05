cards = input().split(" ")
for i in range(5):
    cards[i] = int(cards[i])

points = 0
for i in range(5):
    for j in range(i + 1, 5):
        if cards[i] == cards[j]:
            points += 1

for i in range(0, 4):
    if i == 0:
        total = 0
        for j in range(5):
            total += cards[j]
        if total == 15:
            points += 1
    if i == 1:
        for j in range(5):
            total = 0
            for k in range(5):
                if j != k:
                    total += cards[k]
            if total == 15:
                points += 1

    if i == 2:
        for j in range(5):
            for k in range(j + 1, 5):
                total = 0
                for l in range(5):
                    if l != k and l != j:
                        total += cards[l]
                if total == 15:
                    points += 1

    if i == 3:
        for j in range(5):
            for k in range(j + 1, 5):
                total = cards[j] + cards[k]
                if total == 15:
                    points += 1

print(points)