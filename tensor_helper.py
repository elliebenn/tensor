def is_integer(x):
    if isinstance(x, int):
        return True
    elif isinstance(x, float):
        return x.is_integer() 
    elif isinstance(x, str):
        try:
            f = float(x)
        except ValueError:
            return False
        else:
            return f.is_integer()


def is_numeric(x):
    if isinstance(x, int):
        return True
    elif isinstance(x, float):
        return True
    elif isinstance(x, str):
        try:
            f = float(x)
        except ValueError:
            return False
        return True
    return False


def is_positive(x):
    if not is_integer(x):
        return False
    if x >= 0:
        return True


def all_numbers_in_shape_are_integers_and_positive(shape):
    for num in shape:
        if not is_integer(num):
            return False
        if not is_positive(num):
            return False
    return True