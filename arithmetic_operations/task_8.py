def apples():
    """Returns number of apples that we need to add to split apples whole between friends"""

    friends = int(input())
    apples = int(input())

    # number of apples that needs to be added
    count = 0

    if apples % friends != 0:
        while apples % friends != 0:
            count += 1
            apples += 1
    else:
        count = 0
    print(count)

apples()
