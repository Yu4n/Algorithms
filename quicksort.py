from random import randint


def quicksort(a, p, r):
    if p < r:
        q = partition(a, p, r)
        quicksort(a, p, q - 1)
        quicksort(a, q + 1, r)


def partition(a, p, r):
    pivot = a[r]
    i = p
    # Loop invariant:
    #   1. If p <= k <= i, then a[k] <= pivot.
    #   2. If i + 1 <= k <= j - 1, then a[k] > pivot.
    #   3. If k = r, then a[k] = pivot.
    for j in range(p, r):  # j is from p to r - 1 (inclusive).
        if a[j] <= pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[r] = a[r], a[i]
    return i


def randomized_partition(a, p, r):
    i = randint(p, r)
    a[r], a[i] = a[i], a[r]
    return partition(a, p, r)


def randomized_quicksort(a, p, r):
    if p < r:
        q = randomized_partition(a, p, r)
        randomized_quicksort(a, p, q - 1)
        randomized_quicksort(a, q + 1, r)


def hoare_quicksort(a, p, r):
    if p < r:
        q = hoare_partition(a, p, r)
        hoare_quicksort(a, p, q)
        hoare_quicksort(a, q + 1, r)


def hoare_partition(a, p, r):
    x = a[p]
    i = p - 1
    j = r + 1
    while True:
        while True:
            j -= 1
            if a[j] <= x:
                break
        while True:
            i += 1
            if a[i] >= x:
                break
        if i < j:
            a[i], a[j] = a[j], a[i]
        else:
            return j


A = [2, 8, 7, 1, 3, 5, -2, 6, 4]
hoare_quicksort(A, 0, len(A) - 1)
print(A)
