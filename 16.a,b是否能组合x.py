import math


def combination(x, a, b):
    # 如果x能被a,b组合，则满足ma+nb=x
    k = x // a
    mod = x % a
    if mod == 0:
        return True
    # 如果k != 0,则依次判断 a*i+mod 能否被b整除
    for i in range(k + 1):
        if (a * i + mod) % b == 0:
            return True
    return False  # 否则不能被组合出


a, b = map(int, input().split())
gcd = math.gcd(a, b)
# 求最小公倍数
lcd = a * b // gcd - 1
t = max(a, b)
while lcd >= t:
    if not combination(lcd, a, b):
        print(lcd)
        break
    lcd -= 1
