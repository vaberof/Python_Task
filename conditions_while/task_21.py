def sort():
    """Reads 3 numbers and returns them in non-decreasing order"""
    my_list = []
    for i in range(3):
        a = int(input())
        my_list.append(a)
    my_list.sort()

    for i in my_list:
        print(i)

sort()
