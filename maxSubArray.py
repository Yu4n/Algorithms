import math


def find_max_subarray(a, low, high):
    if low == high:
        return (low, high, a[low])
    else:
        mid = math.floor((low + high) / 2)
        (left_low, left_high, left_sum) = find_max_subarray(a, low, mid)
        (right_low, right_high, right_sum) = find_max_subarray(a, mid + 1, high)
        (cross_low, cross_high, cross_sum) = find_max_crossing_subarray(a, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_low, left_high, left_sum)
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return (right_low, right_high, right_sum)
        else:
            return (cross_low, cross_high, cross_sum)


def find_max_crossing_subarray(a, low, mid, high):
    left_sum, right_sum = - math.inf, - math.inf
    sum = 0
    max_left, max_right = 0, 0
    for i in range(mid, low - 1, -1):
        sum += a[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
    sum = 0
    for j in range(mid + 1, high + 1):
        sum += a[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j
    return (max_left, max_right, left_sum + right_sum)


def maxSubArray_shortest_time(nums):
    '''shortest running time'''
    m = - math.inf
    tempm = - math.inf
    for j in range(len(nums)):
        currHigh = j
        if tempm > 0:
            tempm += nums[j]
        else:
            currLow = j
            tempm = nums[j]
        if tempm > m:
            m = tempm
            low = currLow
            high = currHigh
    return low, high, m
    """
    m = nums[0]
    tempm = nums[0]
    for i in nums[1:]:
        if i > tempm and tempm < 0:
            tempm = i
        else:
            tempm += i
        if tempm > m:
            m = tempm
    return m
    """

def maxSubArray_minimal_memo(nums):
    """Smallest memory needed."""
    max_so_far = nums[0]
    max_ending_here = nums[0]

    for i in range(1, len(nums)):
        max_ending_here = max(max_ending_here + nums[i], nums[i])
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far


def maxSubArray_brutal_force(nums):
    m = - math.inf
    for i in range(len(nums)):
        tempm = 0
        for j in range(i, len(nums)):
            tempm += nums[j]
            if tempm > m:
                m = tempm
                left = i
                high = j
    if m < 0:  # Allow empty subarray.
        return 0
    return left, high, m


ls = [-15, 11, -1, -5, 7, -2, -1, -5, -4]
print(find_max_subarray(ls, 0, len(ls) - 1))
print(maxSubArray_brutal_force(ls))
print(maxSubArray_shortest_time(ls))