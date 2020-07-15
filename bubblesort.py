# In bubble sort algorithm, after each iteration of the loop
# largest element of the array is always placed at right most position.
# Therefore, the loop invariant condition is that at the end of i iteration
# right most i elements are sorted and in place.


def bubbleSort(ls):
    for i in range(len(ls) - 1):
        for j in range(len(ls) - 1, i, -1):
            if ls[j] < ls[j - 1]:
                ls[j], ls[j - 1] = ls[j - 1], ls[j]


a = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]
bubbleSort(a)
print(a)
