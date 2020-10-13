class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        if 'IV' or 'IX' or 'XL' or 'XC' or 'CD' or 'CM' in s:
            fourNum = s.count('IV')
            s = s.replace("IV", '')
            res += 4 * fourNum
            nineNum = s.count('IX')
            s = s.replace('IX', '')
            res += 9 * nineNum
            fortyNum = s.count('XL')
            s = s.replace('XL', '')
            res += 40 * fortyNum
            ninetyNum = s.count('XC')
            s = s.replace('XC', '')
            res += 90 * ninetyNum
            fhNum = s.count('CD')
            s = s.replace('CD', '')
            res += 400 * fhNum
            nhNum = s.count('CM')
            s = s.replace('CM', '')
            res += 900 * nhNum
        res += (s.count('I') + s.count('V') * 5 + s.count('X') * 10 + s.count('L') * 50
                + s.count('C') * 100 + s.count('D') * 500 + s.count('M') * 1000)
        return res

    # From https://leetcode.com/problems/roman-to-integer/discuss/264743/Clean-Python-beats-99.78.
    def romanToInt2(self, s: str) -> int:
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        number = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            number += translations[char]
        return number
