def two_coordinates():
    x = float(input())
    y = float(input())

    k = float(input())
    z = float(input())

    if x * k > 0 and y * z > 0:
        return "YES"
    else:
        return "NO"
print(two_coordinates())
