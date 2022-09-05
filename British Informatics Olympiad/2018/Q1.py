import math
from posixpath import split


debt = 100
interest_rate, repayment_rate = input().split(" ")
interest_rate, repayment_rate = int(interest_rate), int(repayment_rate)
repaid = 0

while (debt != 0):
    debt = debt + math.ceil(debt * interest_rate) / 100
    repayment = math.ceil(debt * repayment_rate) / 100
    
    if repayment < 50:
        repayment = 50
    if repayment > debt:
        repayment = debt

    debt -= repayment
    repaid += repayment

print(repaid)
    