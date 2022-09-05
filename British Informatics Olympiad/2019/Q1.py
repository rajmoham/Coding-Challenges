from operator import truediv


a = int(input())
a_str = str(a)
greater = False

if (len(a_str) % 2 == 0):
    new_a = a_str[0 : int(len(a_str)/2)]

    while greater == False:
        for i in range(len(new_a) - 1, -1, -1):
            new_a += new_a[i]

        if (int(new_a) > a):
            greater = True
        else:
            new_a = new_a[0 : int(len(a_str)/2)]
            new_a = str(int(new_a) + 1)

else:
    new_a = a_str[0 : int(len(a_str)/2 + 1)]

    while greater == False:
        for i in range(len(new_a) - 2, -1, -1):
            new_a += new_a[i]

        if (int(new_a) > a):
            greater = True
        else:
            new_a = new_a[0 : int(len(a_str)/2) + 1]
            new_a = str(int(new_a) + 1)

print(new_a)