# Loop invariant of binary search is:
#   1. left <= right
#   2. A[left] <= target <= A[right]


def binary_search(ls, target):
    left = 0
    right = len(ls) - 1  # right = len(ls) + len(ls) - 2 is still workable
    # Because it doesn't change the loop invariant.
    while left <= right:
        mid = (left + right) // 2  # mid = math.ceil((left + right) / 2) is workable as well.
        if target == ls[mid]:
            return mid
        elif ls[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return None


a = [1, 2, 3, 4, 6, 7, 32, 43]
print(binary_search(a, 5))
print(binary_search(a, 4))
