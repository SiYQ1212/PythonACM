def complete_backpack_with2(goods, weight):
    good_nums = len(goods)
    dp = [[0 for _ in range(weight + 1)] for _ in range(good_nums)]
    for i in range(1, good_nums):
        for j in range(1, weight + 1):
            dp[i][j] = dp[i - 1][j]
            if j >= goods[i][0]:
                dp[i][j] = max(dp[i][j], goods[i][1] + dp[i][j - goods[i][0]])
    return dp[good_nums - 1][weight]


def complete_backpack_with1(goods, weight):
    good_nums = len(goods)
    dp = [0 for _ in range(weight + 1)]
    for i in range(1, good_nums):
        for j in range(goods[i][0], weight + 1):
            dp[j] = max(dp[j], goods[i][1] + dp[j - goods[i][0]])
    return dp[weight]


if __name__ == '__main__':
    # For one item, you can take it multiple times
    goods = [0, [2, 1], [3, 1], [4, 6], [8, 10]]
    weight = 10
    print(complete_backpack_with2(goods, weight))
    print()
    print(complete_backpack_with1(goods, weight))
