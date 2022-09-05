num = int(input())
count = 0

for i in range(2, int(num / 2) + 1):
    isprime = True
    for j in range(2, i):
        if i % j ==0:
            isprime = False
            break
    if isprime == False:
        continue
    for k in range(2, num - i):
        if (num - i) % k == 0:
            isprime = False
            break
    if isprime == True:
        count += 1

print(count)