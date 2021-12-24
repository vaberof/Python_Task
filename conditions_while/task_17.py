def max ():
    a = int(input())
    b = int(input())
    c = int(input())

    if a > b and a > c:
        return a

    if b > a and b > c:
        return b

    if c > a and c > b:
        return c

print(max())
