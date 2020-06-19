def binary_search(ls, target):
    left = 0
    right = len(ls)
    while left <= right:
        mid = (left + right) // 2
        if target == ls[mid]:
            return mid
        elif ls[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return None


a = [1, 2, 3, 4, 6, 7, 32, 43]
print(binary_search(a, 43))
