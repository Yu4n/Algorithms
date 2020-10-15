import math


def cut_rod_recursive(p, n):
    if n == 0:
        return 0
    q = - math.inf
    for i in range(1, n + 1):
        q = max(q, p[i] + cut_rod_recursive(p, n - i))
    return q


prc = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]  # Price
for i in range(0, 11):
    print(cut_rod_recursive(prc, i))
