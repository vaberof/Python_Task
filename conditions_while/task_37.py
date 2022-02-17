cMax = 0
while True:
    a = input()

    if a != ".":
        if float(a) > float(cMax):
            cMax = a
    else:
        print(cMax)
        break
