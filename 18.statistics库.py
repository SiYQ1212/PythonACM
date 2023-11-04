from statistics import *

nums = [i for i in range(1, 11)]
print(mean(nums))  # 算术平均值
print(harmonic_mean(nums))  # 调和平均值
print(median(nums))  # 中位数,两个中位数则取平均值
print(median_low(nums))  # 较小的一个中位数
print(median_high(nums))  # 较大的一个中位数
print(mode(nums))  # 众数
print(pstdev(nums))  # 标准差
print(pvariance(nums))  # 方差
