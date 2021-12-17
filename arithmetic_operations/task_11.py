def percantage():
    money = 100000
    years = int(input())
    sum = 0

    sum = money * ((1 + (10 / 100 / 12)) ** (years * 12))

    return int(sum)
print(percantage())
