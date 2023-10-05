"""
For multiple backpack issues, there is a limit to the number of items per item
"""
# goods = [[2, 1, 6], [6, 10, 6], [3, 6, 3], [weight, value, count]]
def multiple_backpack(goods, weight):
    new_goods = [0]
    for good in goods:
        k = 1
        s = good[2]
        while k <= s:
            new_goods.append([k * good[0], k * good[1]])
            s -= k
            k *= 2
        if s:  # s have value so that the value good[2] is not an integer power of 2
            new_goods.append([s * good[0], s * good[1]])
    # return backpack01_with1List(new_goods, weight)  # 一维01
    return backpack01_with2List(new_goods, weight)  # 二维01


def backpack01_with1List(goods, weight):
    good_nums = len(goods)
    dp = [0 for _ in range(weight + 1)]
    for i in range(1, good_nums):
        for j in range(weight, goods[i][0] - 1, -1):
            dp[j] = max(dp[j], goods[i][1] + dp[j - goods[i][0]])
    return dp[weight]


def backpack01_with2List(goods, weight):
    good_nums = len(goods)
    dp = [[0 for _ in range(weight + 1)] for _ in range(good_nums)]
    for i in range(1, good_nums):
        for j in range(1, weight + 1):
            if j < goods[i][0]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], goods[i][1] + dp[i - 1][j - goods[i][0]])
    return dp[good_nums - 1][weight]


if __name__ == '__main__':
    goods = [[2, 1, 6], [6, 10, 3], [3, 6, 3]]
    print(multiple_backpack(goods, 10))
