num = ["0"]

for i in range(int(input())):
    while True:
        num = int("".join(num))
        num += 1
        num = list(str(num))

        upsidedown = True
        for j in range(len(num)):
            if int(num[j]) + int(num[len(num) - 1 - j]) != 10:
                upsidedown = False
                break
        if upsidedown == True:
            break
print(int("".join(num)))