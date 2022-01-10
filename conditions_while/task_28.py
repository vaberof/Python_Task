def sum_odd_num ():
    k = int(input())
    s = 0
    i = 0
    num = 1
    while i < k:
        if num % 2 == 0:
            num += 1
            continue
        s += num
        num += 1
        i += 1
    return s

print(sum_odd_num())
