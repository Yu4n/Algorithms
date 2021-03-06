import math


def mergesort(a, p, r):
    if p < r:
        q = math.floor((p + r) / 2)
        mergesort(a, p, q)
        mergesort(a, q + 1, r)
        merge(a, p, q, r)


def merge(a, p, q, r):
    # Loop invariant is:
    #   The subarray a[p..k-1] contains k - p smallest elements of
    #       L[1..n1+1] and R[1..n2+1], in sorted order.
    #   Moreover, L[i] and R[j] are the smallest elements
    #       of their arrays that have not been copied into A.
    n1 = q - p + 1  # Length of subarray a[p, q]
    n2 = r - q  # Length of subarray a[q + 1, r]
    left = []
    right = []
    left[:] = a[p: p + n1]  # copy the subarray A[p, q] into L[1, n1]
    right[:] = a[q + 1: q + 1 + n2]   # copy the subarray A[q + 1, r] into R[1, n1]
    left.append(math.inf)
    right.append(math.inf)
    i, j = 0, 0
    for k in range(p, r + 1):
        if left[i] <= right[j]:
            a[k] = left[i]
            i = i + 1
        else:
            a[k] = right[j]
            j = j + 1


ls = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]
# merge(ls, 1, 1, 2)
print(ls)
mergesort(ls, 0, len(ls) - 1)
print(ls)
