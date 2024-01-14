import itertools
from functools import reduce

"""Overall operation"""
standardList = [2, 6, 9, 14, 18]
print(reduce(lambda a, b: a * b, standardList))  # ((((2 * 4) * 6) * 8) * 10)
# print(reduce(mul, standardList))

"""Group deduplication"""
x = list(itertools.groupby("AAADDGGGG"))  # Adjacent grouping
print(x)
m = itertools.groupby([64, 56, 43, 21, 62, 42, 76], lambda x: x % 2 == 0)  # Group by own rule.
for k, v in m:
    print(k, list(v))

"""Prefix"""
d = list(itertools.accumulate(standardList, lambda x, y: (x + 1) * y))  # Prefix
print(d)

"""Sift"""
e = list(filter(lambda x: not x % 3, standardList))
print(e)
f = list(itertools.compress("ABCDEFG", [1, 1, 1, 0, 1, 0, 0]))  # One after the other corresponds to the other, and if it is true, it is reserved
# If there are more sides, the excess is ignored
print(f)
g = list(itertools.dropwhile(lambda x: x < 10, standardList))  # Throw it from scratch until x >= 10
print(g)
h = list(itertools.takewhile(lambda x: x < 10, standardList))  # Hold from the beginning until x<10 is not met
print(h)

"""Take apart"""
print(list(itertools.chain("abc", '123')))
print(list(itertools.chain.from_iterable(['123', '423', 'g34'])))

"""Combine"""
print(list(itertools.starmap(pow, ([2, 5], [3, 4], [5, 2]))))
print(list(itertools.zip_longest("ABC", "123345", fillvalue="/")))
