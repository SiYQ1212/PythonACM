def cal(func):
    def inner(*args, **kwargs):
        t1 = time.time()
        res = func(*args, **kwargs)
        t2 = time.time()
        print(f"{func.__name__} speed {t2 - t1:.8f} s")
        return res

    return inner


@cal
def bubbleSort(nums):
    """O(n^2)"""
    for i in range(len(nums) - 1):
        exchange = False
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                exchange = True
        if not exchange:  # If there is no position swap at the end of a round
            return


@cal
def selectSort(nums):
    """O(n^2)"""
    for i in range(len(nums) - 1):
        min_ind = i
        # Take i as a fixed point and find the smallest number behind it to exchange with it
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_ind]:
                min_ind = j
        nums[i], nums[min_ind] = nums[min_ind], nums[i]


@cal
def insertSort(nums):
    """O(n^2)"""
    for i in range(1, len(nums)):
        tmp = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > tmp:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = tmp


def partition(nums, left, right):
    """Partition the nums array, put the less than [tmp] to the left of [tmp], put the larger than [tmp] to the right of [tmp]
    and finally return the position of [tmp]"""
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


def quickSort(nums, left, right):
    """O(nlogn)"""
    if left < right:
        mid_ind = partition(nums, left, right)
        quickSort(nums, left, mid_ind - 1)
        quickSort(nums, mid_ind + 1, right)


@cal
def quickSortSpeed(nums, left, right):
    quickSort(nums, left, right)


def mergeSort(nums):
    """O(nlogn)"""
    # Split
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    l_list = mergeSort(nums[: mid])
    r_list = mergeSort(nums[mid:])
    # merge
    result = []
    i, j = 0, 0
    while i < len(l_list) and j < len(r_list):
        if r_list[j] < l_list[i]:
            result.append(r_list[j])
            j += 1
        else:
            result.append(l_list[i])
            i += 1
    result += (l_list[i:] + r_list[j:])
    return result


@cal
def mergeSoretSpeed(nums):
    mergeSort(nums)


def heap(nums, n, i):
    # Maintain the properties of the large top heap
    # 'i' is the node subscript to be maintained
    largest, lson, rson = i, i * 2 + 1, i * 2 + 2
    if (lson < n and nums[lson] > nums[largest]):
        largest = lson
    if (rson < n and nums[rson] > nums[largest]):
        largest = rson
    if largest != i:
        # If the child node is larger than the parent node, swap
        nums[largest], nums[i] = nums[i], nums[largest]
        # Recursively perform large heap maintenance on changed nodes
        heap(nums, n, largest)


@cal
def heapSort(nums):
    """O(nlogn)"""
    n = len(nums)
    for i in range(n // 2 - 1, -1, -1):
        heap(nums, n, i)
    for i in range(n - 1, 0, -1):
        nums[0], nums[i] = nums[i], nums[0]
        heap(nums, i, 0)


@cal
def shellSort(nums):
    """O(nlog^2n) ~ O(n^2)"""
    interval = len(nums) // 2
    while interval >= 1:
        '''In fact, it is a range insertion sort'''
        for i in range(interval, len(nums)):
            tmp = nums[i]
            j = i - interval
            while j >= 0 and tmp < nums[j]:
                nums[j + interval] = nums[j]
                j -= interval
            nums[j + interval] = tmp
        interval //= 2


@cal
def bucketSort(nums, bucket_num=10, max_num=1000):
    """O(n + n^2/k + k)   k is bucket_num ==> O(n^2)"""
    # bucket_num is the number of buckets, max_num is the largest number of the array
    buckets = [[] for _ in range(bucket_num)]
    for val in nums:
        # Avoid the number of barrels crossing the line
        i = min(val // (max_num // bucket_num), bucket_num - 1)
        buckets[i].append(val)
    nums.clear()
    for bucket in buckets:
        quickSort(bucket, 0, len(bucket) - 1)
        nums.extend(bucket)


@cal
def countSort(nums, max_num=1000):
    """O(n+k) k is the max_num"""
    # Applies only to sorting of non-negative integers
    count = [0 for _ in range(max_num + 1)]
    for val in nums:
        count[val] += 1
    nums.clear()
    for ind, val in enumerate(count):
        for _ in range(val):
            nums.append(ind)


@cal
def radixSort(nums):
    from collections import deque
    orig = deque(nums)
    nums.clear()
    buckets = [deque() for _ in range(10)]
    n = len(str(max(orig)))
    for i in range(n):
        while orig:
            t = orig.popleft()
            buckets[t // pow(10, i) % 10].append(t)
        if i == n - 1:
            for bucket in buckets:
                while bucket:
                    nums.append(bucket.popleft())
        else:
            for bucket in buckets:
                while bucket:
                    orig.append(bucket.popleft())


if __name__ == '__main__':
    import random, time

    n = 10 ** 5
    nums = [i for i in range(n)]
    random.shuffle(nums)
    # bubbleSort(nums[:])
    # selectSort(nums[:])
    # insertSort(nums[:])
    quickSortSpeed(nums[:], 0, len(nums) - 1)
    mergeSoretSpeed(nums[:])
    heapSort(nums[:])
    shellSort(nums[:])
    bucketSort(nums[:], max_num=n)
    countSort(nums[:], max_num=n)
    radixSort(nums[:])
