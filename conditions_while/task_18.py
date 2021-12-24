def king ():
    """Returns number of options of king`s moves"""
    # num of the column
    a = int(input())

    # num of the row
    b = int(input())

    # if king in 1st or in 8th column and upper than 1st row and lower the 8th row
    if a == 1 and b in range (2, 8) or a == 8 and b in range (2, 8):
        return 5

    # if king in the corner
    if a == 1 and b == 1 or a == 1 and b == 8:
        return 3

    # if king in the corner
    if a == 8 and b == 1 or a == 8 and b == 8:
        return 3

    # if king in the 1 row or in the 8th row
    if a in range(2, 8) and b == 1 or a in range(2, 8) and b == 8:
        return 5

    # if king in the center of desk
    if a in range(2, 8) and b in range (2, 8):
        return 8

print(king())
