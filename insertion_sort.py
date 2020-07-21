# Loop invariant is that the subarray A[0 to i-1] is always sorted.
def insertionSort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    # Driver code to test above


def insertionSortRecursive(arr, n):
    # base case
    if n <= 1:
        return

    # Sort first n-1 elements
    insertionSortRecursive(arr, n - 1)
    '''Insert last element at its correct position 
        in sorted array.'''
    key = arr[n - 1]
    j = n - 2

    # Move elements of arr[0..i-1], that are
    # greater than key, to one position ahead
    # of their current position
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j = j - 1

    arr[j + 1] = key


if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6]
    insertionSort(arr)
    print(arr)
    arr2 = [6, 5, 4, 3, 2, 1, 0, -1]
    insertionSortRecursive(arr2, len(arr2))
    print(arr2)
