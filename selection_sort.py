def selection_sort(ls):
    for j in range(len(ls)-1):
        min = j
        for i in range(j + 1, len(ls)):
            if ls[i] < ls[min]:
                min = i
        temp = ls[j]
        ls[j] = ls[min]
        ls[min] = temp


A = [5, 4, 3, 2, 1, 0, -1]
selection_sort(A)
for a in A:
    print(a)
