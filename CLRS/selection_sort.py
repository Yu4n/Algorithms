# Loop invariants are:
#   1. In the outer loop, array is sorted for first i elements.
#   2. In the inner loop, min is always the minimum value in A[i to j].
def selection_sort(ls):
    for j in range(len(ls)-1):
        min = j
        for i in range(j + 1, len(ls)):
            if ls[i] < ls[min]:
                min = i
        ls[j], ls[min] = ls[min], ls[j]


A = [5, 4, 3, 2, 1, 0, -1]
selection_sort(A)
for a in A:
    print(a)
