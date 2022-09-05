from operator import truediv


clock1, clock2 = input().split(" ")
clock1 = int(clock1)
clock2 = int(clock2)

hr1, min1 = 0, 0
hr2, min2 = 0, 0

while True:
    hr1 += 1
    hr2 += 1
    min1 += clock1
    min2 += clock2

    while min1 > 59:
        min1 -= 60
        hr1 += 1

    while min2 > 59:
        min2 -= 60
        hr2 += 1

    while hr1 > 23:
        hr1 -= 24

    while hr2 > 23:
        hr2 -= 24

    if (hr1 == hr2) and (min1 == min2):
        break

def TimeFormat(hour, minute):
    outputTime = ""
    if hour < 10:
        outputTime += "0" + str(hour)
    else:
        outputTime += str(hour)

    outputTime += ":"

    if minute < 10:
        outputTime += "0" + str(minute)
    else:
        outputTime += str(minute)

    return outputTime

print(TimeFormat(hr1, min1))