def quicksort(a, p, r):
    if p < r:
        q = partition(a, p, r)
        quicksort(a, p, q - 1)
        quicksort(a, q + 1, r)


def partition(a, p, r):
    pivot = a[r]
    i = p - 1
    # Loop invariant:
    #   1. If p <= k <= i, then a[k] <= pivot.
    #   2. If i + 1 <= k <= j - 1, then a[k] > pivot.
    #   3. If k = r, then a[k] = pivot.
    for j in range(p, r):
        if a[j] <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[r] = a[r], a[i + 1]
    return i + 1


A = [5, 4, 3, 2, 1, 0, -1]
quicksort(A, 0, len(A) - 1)
print(A)
