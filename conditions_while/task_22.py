def Fizz_Buzz ():
    a = int(input())

    if a % 3 == 0 and a % 5 == 0:
        return "Fizz Buzz"

    if a % 3== 0:
        return "Fizz"

    if a % 5 == 0:
        return "Buzz"

    return a

print(Fizz_Buzz())
