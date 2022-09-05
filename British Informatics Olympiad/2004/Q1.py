isbn = input()

missing = ""
sum = 0

for i in range(10):
    if isbn[i] == "?":
        missing = 10 - i
    else:
        if isbn[i] == "X":
            sum += 10 * (10 - i)
        else:
            sum += int(isbn[i]) * (10 - i)
            
count = 0
while sum % 11 != 0:
    sum += missing
    count += 1

if count == 10:
    count = "X"

print(count)