print("aBcdE".swapcase())  # 大写转小写，小写转大写
print("aBcdE".lower(), "aBcdE".upper())  # 全部转小写  or  全部转大写
print("happy".casefold())  # 适用更广的小写转换
print("123".isdigit())  # 检查字符串中的字符是否都是数字
print("aBcdE".isalpha())  # 检查字符串中的字符是否都是字母
print("sy12".isalnum())  # 检查字符串中的字符是否都是字母或者数字
print("1 2 3".isspace())  # 检查字符串中的字符是否都是空格
print("aBcdE".capitalize())  # 返回副本，首字母大写
print("1 2 3".split())  # 默认以空格分隔
print("123".partition('2'))  # 分割但包含分割字符
print(" ".join(['a', 'c', 'e']))  # 连接可迭代对象的所有元素
print("1 2 3".replace('3', '4'))  # 用一个字符串代替另一个字符串
print("123".center(20))  # 将字符串打印在中间
print("123".index("2"))  # 查找第一个"2"的位置,找不到则报错
print("123".find("0"))  # 查找子串（sub）在字符串中的第一次出现的位置，返回索引，如果找不到则返回-1。
print("12344".count("4"))  # 计数
print("happy".title())  # 将字符串中每个单词的首字母转换为大写，其余字符转换为小写。
print(" happy ".strip())  # 去除字符串两端的空白字符（空格、制表符、换行符等）。
print(" happy ".lstrip())  # 去除字符串左端的空白字符。
print(" happy ".rstrip())  # 去除字符串右端的空白字符。
print("happy".startswith("h"))  # 检查字符串是否以指定的前缀开头，返回布尔值。
print("happy".endswith("py"))  # 检查字符串是否以指定的后缀结尾，返回布尔值。
