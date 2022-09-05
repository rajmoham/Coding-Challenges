from operator import truediv


password = input()
half_chars = len(password) // 2
incorrect = False

for i in range(half_chars):
    last_char = ""
    for j in range(0, len(password), i+1):
        if (password[j:j+i+1] == last_char):
            incorrect = True
            break
        else:
            last_char = password[j:j+i+1]

    if (incorrect == True):
        break
if (incorrect == True):
    print("Rejected")
else:
    print("Accepted")