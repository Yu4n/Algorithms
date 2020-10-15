import math


def cut_rod_recursive(p, n):
    if n == 0:
        return 0
    q = - math.inf
    for i in range(1, n + 1):
        q = max(q, p[i] + cut_rod_recursive(p, n - i))
    return q


def memoized_cut_rod(p, n):
    r = [-1 for _ in range(n + 1)]

    return memoized_cut_rod_aux(p, n, r)


def memoized_cut_rod_aux(p, n, r):
    if r[n] >= 0:
        return r[n]
    q = p[0]
    if n == 0:
        q = 0
    else:
        for i in range(1, n + 1):
            q = max(q, p[i] + memoized_cut_rod_aux(p, n - i, r))

    r[n] = q
    return q


def bottom_up_cut_rod(p, n):
    r = [0 for _ in range(n + 1)]

    for j in range(1, n + 1):
        q = p[0]
        for i in range(1, j + 1):
            q = max(q, p[i] + r[j - i])
        r[j] = q

    return r[n]


prc = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]  # Price
for i in range(0, 11):
    print(bottom_up_cut_rod(prc, i))
