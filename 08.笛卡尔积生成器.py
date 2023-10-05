import itertools


def multi_cycle():
    for i in range(10):
        for j in range(10):
            for k in range(10):
                if i == j == k:
                    return 1
    return 0


# Shorthand for multi-layer loops
# This facilitates the inner loop to jump directly out of the multi-layer cycle

all_list = [range(10), range(10), range(10)]
# for i, j, k in itertools.product(range(10), range(10), range(10)):
for i, j, k in itertools.product(*all_list):
    if i == j == k == 5:
        break
    print(i, j, k)
