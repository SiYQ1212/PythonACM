def bubleSort(nums):  # O(n^2)
    for i in range(len(nums) - 1):
        exchange = False
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                exchange = True
        if not exchange:  # If there is no position swap at the end of a round
            return


def selectSort(nums):  # O(n^2)
    for i in range(len(nums) - 1):
        min_ind = i
        # Take i as a fixed point and find the smallest number behind it to exchange with it
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_ind]:
                min_ind = j
        nums[i], nums[min_ind] = nums[min_ind], nums[i]


def insertSort(nums):  # O(n^2)
    for i in range(1, len(nums)):
        tmp = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > tmp:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = tmp


def partition(nums, left, right):
    # Partition the nums array, put the less than [tmp] to the left of [tmp], put the larger than [tmp] to the right of [tmp]
    # and finally return the position of [tmp]
    tmp = nums[left]
    while left < right:
        while left < right and nums[right] >= tmp:
            right -= 1
        nums[left] = nums[right]
        while left < right and nums[left] <= tmp:
            left += 1
        nums[right] = nums[left]
    nums[left] = tmp
    return left


def quickSort(nums, left, right):  # O(nlogn)
    if left < right:
        mid_ind = partition(nums, left, right)
        quickSort(nums, left, mid_ind - 1)
        quickSort(nums, mid_ind + 1, right)


if __name__ == '__main__':
    nums = [5, 7, 4, 6, 3, 1, 2, 9, 8]
    # bubleSort(nums)
    # selectSort(nums)
    # insertSort(nums)
    quickSort(nums, 0, len(nums) - 1)
    print(nums)
