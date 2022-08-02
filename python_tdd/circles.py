from math import pi

def circle_area(r):
    # 1st implementation
    """
    return pi * (r ** 2)
    """

    # 2nd implementation
    """
    if r < 0:
        raise ValueError("The radius cannot be negative.")
    return pi * (r ** 2)
    """

    # 3rd implementation
    if type(r) not in [int, float]:
        raise TypeError("The radius must be a non-negative real number.")
    if r < 0:
        raise ValueError("The radius cannot be negative.")
    return pi * (r ** 2)
