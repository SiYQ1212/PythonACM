from itertools import combinations

org = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']  # total num is eight
"""
00000000  Indicates that none is selected
11111111  Indicates that all are selected
"""
for i in range(0, 256):
    s = "%08d" % int(str(bin(i)[2:]))
    do = []
    for ind, flag in enumerate(s):
        if flag == "1":
            do.append(org[ind])
    print(do)

# Import libraries
for i in range(len(org) + 1):
    for j in combinations(iterable=org, r=i):
        print(j)
