# F0 = 0
# F1 = 1
# 0 1 1 2 3 5 8 13 21
def fib ():
    n = int(input())

    if n == 0:
        return 0
    if n == 1:
        return 1
        
    F0 = 0
    F1 = 1
    i = 1
    s = 0

    while i < n:
        s = F0 + F1
        F0 = F1
        F1 = s
        i += 1
    return s
print(fib())
