class Solution:
    def secondHighest(self, s: str) -> int:
        highest = None
        for char in s:
            if ord(char) <= 57:
                if not highest:
                    highest = char
                elif char > highest:
                    highest = char
        second = None
        for char in s:
            if ord(char) <= 57:
                if second and highest > char > second:
                    second = char
                elif not second:
                    if char < highest:
                        second = char
        return second if second else -1
