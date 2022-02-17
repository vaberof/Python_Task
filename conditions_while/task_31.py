# 0 1 1 2 3 5 8 13 21 34 ...
def fib_nums():
    n = int(input())

    if n == 0:
        return 0
    if n == 1:
        return 1

    F0 = 0
    F1 = 1
    fibNums = [F0, F1]
    F3 = 0

    while n != F3:
        F3 = F0 + F1
        F0 = F1
        F1 = F3
        fibNums.append(F3)

        if F3 == n:
            return fibNums.index(F3)

        if n < F3 and n not in fibNums:
            return "no"

print(fib_nums())
