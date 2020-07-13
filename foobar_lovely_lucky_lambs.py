def solution(total_lambs):
    i = stingy(total_lambs)
    j = generous(total_lambs)
    return i - j


def generous(total_lambs):
    sum_lambs, i = 0, 0
    while sum_lambs <= total_lambs:
        sum_lambs += 2 ** i
        i += 1
    return i - 1


def stingy(total_lambs):
    i, j = 0, 1
    cnt, sum_lambs = 0, 0
    while sum_lambs <= total_lambs:
        sum_lambs += j
        i, j = j, i + j
        cnt += 1
    cnt -= 1
    return cnt
