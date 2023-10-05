def mul():
    """
    n >> m  <==>  n // pow(2, m)
    :return:
    """
    a = (16 // 2)
    b = (16 >> 1)
    return a, b


def mod():
    """
    n % 2 == 0  <==>  n & 1 == 0
    :return:
    """
    a = (8 % 2 == 0)
    b = (8 & 1 == 0)
    return a, b


def mic():
    """
    2 ** n  <==>  1 << n
    :return:
    """
    a = 2 ** 5
    b = 1 << 5
    return a, b


if __name__ == '__main__':
    print(mul())
    print(mod())
    print(mic())
