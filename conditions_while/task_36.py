s = 0
massive = []
while True:
    a = input()
    if a != ".":
        massive.append(float(a))
    else:
        length = len(massive)
        for i in range(0, length, 2):
            s += massive[i]
        print(s)
        break
