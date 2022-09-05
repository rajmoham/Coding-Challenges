from itertools import product

score, drats = input().split(" ")
score, drats = int(score), int(drats)

if drats == 0:
    print(0)
else:
    if score%2 == 0:
        max = score - 2
    else:
        max = score - 3
    if max > 40:
        max = 40
        
    first_pos = [j for j in range(2, max + 1, 2)]
    count = 0
    for i in first_pos:
        temp_score = score - i

        combs = [(j+1) for j in range(temp_score - (drats - 2)) if j < 20]

        drat_combs = list(product(combs, repeat=(drats-1)))

        for j in drat_combs:
            total = 0
            for k in j:
                total += int(k)
            if (total == temp_score):
                count += 1

print(count)
