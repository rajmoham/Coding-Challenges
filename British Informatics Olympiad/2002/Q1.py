friends = int(input())
rhyme = int(input())

circle = []

for i in range(friends):
    circle.append(i + 1)

index = 0
while len(circle) > 1:
    index += rhyme
    while index > len(circle) - 1:
        index -= len(circle)
    del circle[index]

    index += 1

print(circle[0])