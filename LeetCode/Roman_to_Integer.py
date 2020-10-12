class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        newstr = ''
        if 'IV' or 'IX' or 'XL' or 'XC' or 'CD' or 'CM' in s:
            fourNum = s.count('IV')
            newstr = s.replace("IV", '')
            res += 4 * fourNum
            nineNum = s.count('IX')
            newstr = newstr.replace('IX', '')
            res += 9 * nineNum
            fortyNum = s.count('XL')
            newstr = newstr.replace('XL', '')
            res += 40 * fortyNum
            ninetyNum = s.count('XC')
            newstr = newstr.replace('XC', '')
            res += 90 * ninetyNum
            fhNum = s.count('CD')
            newstr = newstr.replace('CD', '')
            res += 400 * fhNum
            nhNum = s.count('CM')
            newstr = newstr.replace('CM', '')
            res += 900 * nhNum
        res += (newstr.count('I') + newstr.count('V') * 5 + newstr.count('X') * 10 + newstr.count('L') * 50
                + newstr.count('C') * 100 + newstr.count('D') * 500 + newstr.count('M') * 1000)
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
