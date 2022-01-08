def two_coordinates():
    x = float(input())
    y = float(input())

    k = float(input())
    z = float(input())

    # 1 четверть
    if x > 0 and y > 0:
        if k > 0 and z > 0:
            return "YES"
        else:
            return "NO"

    # 4 четверть
    if x > 0 and y < 0:
        if k > 0 and z < 0:
            return "YES"
        else:
            return "NO"

    # 2 четверть
    if x < 0 and y > 0:
        if k < 0 and z > 0:
            return "YES"
        else:
            return "NO"

    # 3 четверть
    if x < 0 and y < 0:
        if k < 0 and z < 0:
            return "YES"
        else:
            return "NO"

print(two_coordinates())
