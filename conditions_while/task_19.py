def king():
    """Returns number of options"""
    # num of the column // START POS
    a = int(input())
    # num of the row // START POS
    b = int(input())

    # num of the column // END POS
    c = int(input())
    # num of the row // END POS
    d = int(input())

    if a == c and b == d:
        return "NO"

    # if king in 1st or in 8th column and upper than 1st row and lower the 8th row
    if a == 1 and b in range(2, 8):
        if c in range(a, a + 2) and d in range(b - 1, b + 2):
            return "YES"
        else:
            return "NO"

    # if king in 1st or in 8th column and upper than 1st row and lower the 8th row
    if a == 8 and b in range(2, 8):
        if c in range(a - 1, a + 1) and d in range(b - 1, b + 2):
            return "YES"
        else:
            return "NO"

    # if king in 1st row and not in the corner
    if a in range(2, 8) and b == 1:
        if c in range(a - 1, a + 2) and d in range(b, b + 2):
            return "YES"
        else:
            return "NO"

    # # if king in 8th row and not in the corner
    if a in range(2, 8) and b == 8:
        if c in range(a - 1, a + 2) and d in range(b - 1, b + 2):
            return "YES"
        else:
            return "NO"

    # if king in the corner
    if a == 1 and b == 1:
        if c in range(a, a + 2) and d in range(1, b + 2):
            return "YES"
        else:
            return "NO"

    # if king in the corner
    if a == 1 and b == 8:
        if c in range(a, a + 2) and d in range(7, b + 2):
            return "YES"
        else:
            return "NO"

    # if king in the corner
    if a == 8 and b == 1:
        if c in range(7, a + 1) and d in range(b, b + 2):
            return "YES"
        else:
            return "NO"
            
    # if king in the corner
    if a == 8 and b == 8:
        if c in range(7, a + 1) and d in range(b, b + 1):
            return "YES"
        else:
            return "NO"

    # if king in the center of desk
    if a in range(2, 8) and b in range(2, 8):
        if c in range(a - 1, a + 2) and d in range (b - 1, b + 2):
            return "YES"
        else:
            return "NO"

print(king())
