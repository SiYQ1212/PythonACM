def backpack01_with2List(goods, weight):
    """
    :param goods: Receive a two-dimensional list with each listing the weight and value of the item
    :param weight: An integer that represents the maximum weight that can fit in the backpack
    :return: Returns an integer representing the maximum value of the item obtained within the limit of weight
    """
    good_nums = len(goods)
    dp = [[0 for _ in range(weight + 1)] for _ in range(good_nums)]
    for i in range(1, good_nums):
        for j in range(1, weight + 1):
            if j < goods[i][0]:
                # If the weight of the current backpack is less than the weight of the item in this cycle,
                # the optimal solution inherits the optimal solution of the item with less weight of the backpack
                dp[i][j] = dp[i - 1][j]
            else:
                # If the current backpack is larger or equal to the weight of the item，
                # value = max (do not take the item, take the item (item + the optimal solution of the limit of the previous round of backpack minus the weight of the item))
                dp[i][j] = max(dp[i - 1][j], goods[i][1] + dp[i - 1][j - goods[i][0]])
    return dp[good_nums - 1][weight]


def backpack01_with1List(goods, weight):
    good_nums = len(goods)
    dp = [0 for _ in range(weight + 1)]
    for i in range(1, good_nums):
        for j in range(weight, goods[i][0] - 1, -1):
            dp[j] = max(dp[j], goods[i][1] + dp[j - goods[i][0]])
    return dp[weight]


if __name__ == '__main__':
    # For one item can only be taken once
    goods = [0, [2, 3], [3, 5], [4, 6], [5, 8], [6, 9]]
    weight = 15
    print(backpack01_with2List(goods, weight))
    print()
    print(backpack01_with1List(goods, weight))
