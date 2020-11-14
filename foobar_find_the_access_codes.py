def solution(l):
    count = 0
    n = len(l)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                p = l[k] / l[j]
                q = l[j] / l[i]
                if (p % 1 == 0) and (q % 1 == 0):
                    count += 1
    return count


l = [1, 2, 3, 4, 5, 6]
print(solution(l))
