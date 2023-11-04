def my_all():
    arr = list(range(100))
    for i in arr:
        if i % 5 == 0:
            return 0
    return 1


def sys_all():
    arr = list(range(100))
    return all(item % 5 for item in arr)


if __name__ == '__main__':
    # For a wide range of judgments, "all" and "any" will be faster than handwritten judgments
    print(my_all(), sys_all())

