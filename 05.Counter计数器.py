from collections import Counter
from random import randint
from time import perf_counter

string = ""
for _ in range(40_0000):
    string += str(randint(0, 9))

t1 = perf_counter()
dc = {}
for i in string:
    if dc.get(i):
        dc[i] += 1
    else:
        dc[i] = 1

t2 = perf_counter()
dc_0 = Counter(string)
t3 = perf_counter()

print(t2 - t1)
print(t3 - t2)
# Counters are faster than manually implementing counters
