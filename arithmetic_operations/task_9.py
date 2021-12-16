def triangle_area():
    """Returns area of a triangle"""

    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())

    # general area of a triangle
    general_area = (d + b) * (c + a)

    # a part of a triangle
    part_area = b * c
    
    result = general_area - part_area

    print(result)

triangle_area()
