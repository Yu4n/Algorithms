# https://leetcode.com/problems/regular-expression-matching/

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        ns = len(s)
        np = len(p)
        memo = {}

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if j == np:
                if i == ns:
                    return True
                else:
                    return False
            if i == ns:
                if (np - j) % 2 == 1:
                    return False
                else:
                    for k in range(j + 1, np, 2):
                        if p[k] != '*':
                            return False
                    return True
            if p[j] in {s[i], '.'}:
                if j + 1 < np and p[j + 1] == '*':
                    res = dp(i, j + 2) or dp(i + 1, j)
                else:
                    res = dp(i + 1, j + 1)
            elif p[j] not in {s[i], '.'}:
                if j + 1 < np and p[j + 1] == '*':
                    res = dp(i, j + 2)
                else:
                    res = False
            memo[(i, j)] = res
            return res

        return dp(0, 0)
