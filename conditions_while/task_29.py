# подается число на вход
# провярем делители числа в диапозоне от 1 до самого числа
# если делителей 2: число простое
# если больше: число непростое

def isPrime ():
    n = int(input())
    i = 1
    count = 0
    while i <= n:
        if n % i == 0:
            count += 1
        i += 1

    if count > 2:
        return "composite"

    if count == 2:
        return "prime"

print(isPrime())
