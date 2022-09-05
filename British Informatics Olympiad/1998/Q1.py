numerals = [[1000, "M"], [900,"CM"], [500, "D"], [400, "CD"], [100, "C"], [90, "XC"] ,
            [50, "L"], [40, "XL"], [10, "X"], [9, "IX"], [5, "V"], [4, "IV"], [1, "I"]]

num = input()
digits = []
romans = ""

for i in range(len(num)):
    digits.append(int(num[i] + "0"*(len(num) - i - 1)))

    for i in range(len(digits)):
        while digits[i] != 0:
            highest = 0
            character = ""
            for j in numerals:
                if digits[i] >= j[0]:
                    romans += j[1]
                    digits[i] -= j[0]
                    break
print(romans)