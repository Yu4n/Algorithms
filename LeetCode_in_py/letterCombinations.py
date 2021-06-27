class Solution:
    def letterCombinations(self, digits):
        if '' == digits:
            return []
        key = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        res = ['']
        for c in digits:
            tmp = []
            for y in res:
                for x in key[c]:
                    tmp.append(y + x)
            res = tmp
        return res

    def letterCombinationsQueue(self, digits: str) -> [str]:
        if not digits: return []
        phone = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        queue = ['']  # 初始化队列
        for digit in digits:
            for _ in range(len(queue)):
                tmp = queue.pop(0)
                for letter in phone[ord(digit) - 50]:  # 这里我们不使用 int() 转换字符串，使用ASCII码
                    queue.append(tmp + letter)
        return queue

    def letterCombinationsRecur(self, digits: str) -> [str]:
        mapping = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return [i for i in mapping[int(digits)]]
        ans = []
        for i in mapping[int(digits[0])]:
            ans += [i + s for s in self.letterCombinations(digits[1:])]
        return ans
