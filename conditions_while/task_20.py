def color():
    a = int(input())
    b = int(input())
    if (a + b) % 2 == 0:
        return "BLACK"
    else:
        return "WHITE"
print(color())
