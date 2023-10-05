from functools import cmp_to_key

List = [(5, 4), (7, 3), (3, 5), (3, 7), (7, 2), (5, 5), (6, 3)]
List.sort()
# Normal sorting, the default is to sort according to the first one from smallest to largest,
# and then sort according to the second
print(List)

List.sort(key=lambda x: x[1])
# Sort from smallest to largest according to the second number
print(List)


def cmp(a, b):
    # Sort first according to the first one from largest to smallest, and then sort according to the second
    if a[0] > b[0]:
        return -1
    elif a[0] < b[0]:
        return 1
    else:
        if a[1] > b[1]:
            return 1
        elif a[1] < b[1]:
            return -1
        else:
            return 0


List.sort(key=cmp_to_key(cmp))
print(List)
