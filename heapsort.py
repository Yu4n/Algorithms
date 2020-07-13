# Python program for implementation of heap Sort

# To heapify subtree rooted at index i. 
# n is size of heap 
def heapify(arr, n, i):
    largest = i  # Initialize largest as root 
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is 
    # greater than root 
    if l < n and arr[i] < arr[l]:
        largest = l

        # See if right child of root exists and is
    # greater than root 
    if r < n and arr[largest] < arr[r]:
        largest = r

        # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root. 
        heapify(arr, n, largest)

    # The main function to sort an array of given size


def heapSort(arr):
    n = len(arr)

    # Build a maxheap. 
    # Since last parent will be at ((n//2)-1) we can start at that location. 
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

        # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)


def max_heapify(a, n, i):
    heapSize = n
    left = 2 * i + 1
    right = 2 * i + 2
    if left < heapSize and a[i] < a[left]:
        largest = left
    else:
        largest = i
    # if a[largest] < a[right] and right < heapSize:
    # Be careful of the conditional statement above which causes list out of range!
    if right < heapSize and a[largest] < a[right]:
        largest = right
    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        max_heapify(a, n, largest)


def build_max_heap(a):
    for i in range(len(a) // 2 - 1, -1, -1):
        max_heapify(a, len(a) - 1, i)


def heapsort(a):
    build_max_heap(a)
    for i in range(len(a) - 1, 0, -1):
        a[0], a[i] = a[i], a[0]
        max_heapify(a, i, 0)


if __name__ == '__main__':
    arr = [12, 11, 13, 20, 20, 50, 7, 4, 3, 2, 1, -1]
    heapsort(arr)
    print(arr)
