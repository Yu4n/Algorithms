def counting_sort(a):
    k = max(a) - min(a) + 1
    b, c = [], []  # c is the counting array, and b is the sorted array.
    '''for i in range(k):
        c.append(0)'''
    c = [0] * k
    '''for i in range(len(a)):
        b.append(0)'''
    b = [0] * len(a)
    for j in range(len(a)):
        c[a[j]] = c[a[j]] + 1
    for i in range(1, k):
        c[i] = c[i] + c[i - 1]
    for j in range(len(a) - 1, -1, -1):
        b[c[a[j]] - 1] = a[j]
        c[a[j]] -= 1
    return b


if __name__ == '__main__':
    A = [2, 5, 3, 0, 2, 3, 0, 3]
    print(counting_sort(A))
