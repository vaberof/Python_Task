def coordinate():
    x = float(input())
    y = float(input())

    # 1 четверть
    if x >= 0 and y > 0:
        return 1

    # 4 четверть
    if x >= 0 and y < 0:
        return 4

    # 2 четверть
    if x <= 0 and y > 0:
        return 2

    # 3 четверть
    if x <= 0 and y < 0:
        return 3

print(coordinate())
