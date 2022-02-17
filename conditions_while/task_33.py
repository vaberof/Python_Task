s = 0
while True:
    a = input()
    if a != ".":
        s += int(a)
    if a == ".":
        print(s)
        break
