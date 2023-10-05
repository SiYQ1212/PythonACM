"""
For an array, we need to perform a large number of interval addition and subtraction operations.
and use the difference method to modify the prefix and array to find the array at the end of the final operation
"""
from itertools import accumulate
arr = [0] * 20
pre_arr = arr[:]  # Prefix and array
print(arr, "++++", pre_arr)
# Add 3 to the [4, 8) interval
pre_arr[4] = 3
pre_arr[8] = -3
print(list(accumulate(pre_arr)), "++++", pre_arr)

# Minus 5 in the [5, 10) interval
pre_arr[5] = -5
pre_arr[10] = 5
print(list(accumulate(pre_arr)), "++++", pre_arr)

# Add 8 to the [14, 20] interval
# When the end of the operation interval is the end of the array, omit the operation of trailing inverses
pre_arr[14] = 8
print(list(accumulate(pre_arr)), "++++", pre_arr)
