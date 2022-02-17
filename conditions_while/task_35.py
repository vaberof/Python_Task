s = 0

while True:
    sqrt = 0
    a = input()
    if a != ".":
        b = float(a)
        sqrt = b**2
        s += sqrt
    else:
        print(s)
        break
