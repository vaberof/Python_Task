def apples():
    """
    Returns:
    1) The nubmer of whole apples each friend
    2) The number of apples which will be unseparated
    3) The number of apples that will get each friend if they will divide apples
    """
    # number of friends
    friends = int(input())
    # number of apples
    apples = int(input())

    # number of whole apples
    whole = apples // friends

    # number of unseparated apples
    if whole != 0:
        unseparated = apples - whole * friends
    else:
        unseparated = apples

    # number of divided apples
    divided =  apples / friends

    return(f"{whole}\n{unseparated}\n{divided}")

print(apples())
