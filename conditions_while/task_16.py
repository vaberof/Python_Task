def students ():
    """Returns correct form of the word 'student' in Latin"""
    x = int(input())

    # если остаток 0
    if x % 10 == 0:
        print(x, "studentov")
        return

    # если остаток от 2 до 4, проверяем не двузначное ли число в остатке
    if x % 10 in range(2, 5):
        if x % 100 in range(11, 21):
            print(x, "studentov")
            return
        else:
            print(x, "studenta")
            return

    # если остаток от 5 до 10
    if x % 10 in range(5, 11):
        print(x, "studentov")
        return

    # если остаток 1, то проверяем не двузначное ли число в остатке
    if x % 10 == 1:
        if x % 100 in range(11, 21):
            print(x, "studentov")
            return
        else:
            print(x, "student")
            return

    # если остаток от 11 до 20
    if x % 100 in range(11, 21):
        print(x, "studentov")
        return

    # если остаток входит в данные промежутки
    if x % 100 in range(22, 25) or x % 100 in range(32, 35) or x % 100 in range(42, 45)\
    or x % 100 in range(52, 55) or x % 100 in range(62, 65) or x % 100 in range(72, 75)\
    or x % 100 in range(82, 85) or x % 100 in range(92, 95):
        print(x, "studenta")
        return

students()
