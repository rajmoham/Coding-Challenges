combs = []
combs.append(input())
count = 0

def LeftToMid(clothes):
    temp = clothes[0]
    del clothes[0]
    clothes.insert(3, temp)
    return "".join(clothes)

def RightToMid(clothes):
    temp = clothes[6]
    del clothes[6]
    clothes.insert(3, temp)
    return "".join(clothes)

def MidToLeft(clothes):
    temp = clothes[3]
    del clothes[3]
    clothes.insert(0, temp)
    return "".join(clothes)

def MidToRight(clothes):
    temp = clothes[3]
    del clothes[3]
    clothes.append(temp)
    return "".join(clothes)

while "1234567" not in combs:
    new_list = []
    for i in range(len(combs)):
        new_list.append(LeftToMid(list(combs[i])))
        new_list.append(RightToMid(list(combs[i])))
        new_list.append(MidToLeft(list(combs[i])))
        new_list.append(MidToRight(list(combs[i])))

    del combs
    combs = new_list
    count += 1

print(count)
