class Solution:
    def isValid(self, s: str) -> bool:
        ls = []
        for x in s:
            if not ls:
                ls.append(x)
            elif x == ')' and ls[-1] == '(':
                ls.pop()
            elif x == '}' and ls[-1] == '{':
                ls.pop()
            elif x == ']' and ls[-1] == '[':
                ls.pop()
            else:
                ls.append(x)
        if ls:
            return False
        else:
            return True


x = Solution()
ss = "()"
print(x.isValid(ss))
