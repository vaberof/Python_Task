s = 0
n = 0
while True:
    a = input()
    if a != ".":
        s += int(a)
        n +=1
    if a == ".":
        print(s / n)
        break
