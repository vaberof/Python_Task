massive = []

while True:
    a = input()

    if a != ".":
        massive.append(float(a))
    else:
        massive.sort()
        print(massive[-2])
        break
