def percantage():
    money = 100000
    years = int(input())

    for i in range(years):
        sum = money + ((10 / 100) * money)
        if years > 1:
            for y in range(years - 1):
                sum = sum + ((10 / 100) * sum)

    print(int(sum))

percantage()
