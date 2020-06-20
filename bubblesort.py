def bubbleSort(ls):
    for i in range(len(ls) - 1):
        for j in range(len(ls) - 1, i, -1):
            if ls[j] < ls[j - 1]:
                temp = ls[j]
                ls[j] = ls[j - 1]
                ls[j - 1] = temp


a = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]
bubbleSort(a)
print(a)












