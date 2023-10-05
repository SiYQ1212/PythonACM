def the_longest_palindromic_substring(s: str):
    max_len = 0
    start = 0
    str_len = len(s)
    dp = [[False] * str_len for _ in range(str_len)]
    for i in range(str_len - 1, -1, -1):
        for j in range(i, str_len):
            if s[i] == s[j]:
                if j - i <= 1 or dp[i + 1][j - 1]:
                    dp[i][j] = True
                    if j - i + 1 > max_len:
                        max_len = j - i + 1
                        start = i
    return s[start: start + max_len]


if __name__ == '__main__':
    print(the_longest_palindromic_substring("weizhaoshigeddedashabi"))
