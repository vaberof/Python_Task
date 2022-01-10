def square_k_num ():
    k = int(input())
    s = 0
    i = 0
    num = 1
    while i < k:
        s += (num ** 2)
        num += 1
        i += 1
    return s
print(square_k_num())
