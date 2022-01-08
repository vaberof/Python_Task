def point_inside():
    x = float(input())
    y = float(input())

    r = float(input())
    if (x ** 2) + (y ** 2) <= (r ** 2):
        return "YES"
    else:
        return "NO"

print(point_inside())
