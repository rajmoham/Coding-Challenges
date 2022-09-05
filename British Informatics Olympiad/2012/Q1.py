number = int(input())
temp_num = number

primes = []
factors = []

while temp_num != 1:
    temp_num = int(temp_num)
    for i in range(2, temp_num + 1):
        isPrime = True
        for j in range(2, i):
            if (i%j == 0):
                isPrime = False
                break
        if (isPrime == True):
            if temp_num % i == 0:
                temp_num /= i
                if i in factors:
                    break
                else:
                    factors.append(i)
                    break

product = 1

for i in range(len(factors)):
    product *= factors[i]

print(product)