import math


def max_heapify(a, n, i):
    heapSize = n
    left = 2 * i + 1
    right = 2 * i + 2
    if left < heapSize and a[i] < a[left]:
        largest = left
    else:
        largest = i
    # if a[largest] < a[right] and right < heapSize:
    # Be careful of the conditional statement above, which causes list out of range!
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


def heap_maximum(a,):
    return a[0]


def heap_extract_max(a, heapsize=None):
    if heapsize is None:
        heapsize = len(a)
    if heapsize < 1:
        return -1
    max_value = a[0]
    a[0] = a[heapsize - 1]
    del(a[heapsize - 1])
    heapsize -= 1
    max_heapify(a, heapsize, 0)
    return max_value


def heap_increase_key(a, i, key):
    if key < a[i]:
        return -1
    a[i] = key
    while i > 0 and a[(i - 1) // 2] < a[i]:
        a[i], a[(i - 1) // 2] = a[(i - 1) // 2], a[i]
        i = (i - 1) // 2


def max_heap_insert(a, key):
    a.append(- math.inf)
    heap_increase_key(a, len(a) - 1, key)


if __name__ == '__main__':
    arr = [12, 11, 13, 20, 20, 50, 7, 4, 3, 2, 1, -1]
    build_max_heap(arr)
    print(arr)
    heap_increase_key(arr, len(arr) - 1, 100)
    print(arr)
    max_heap_insert(arr, 101)
    print(arr)
