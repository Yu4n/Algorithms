class Solution:
    def majorityElement(self, nums) -> int:
        votes = 0
        x = None
        for num in nums:
            if votes == 0:
                x = num
            votes += 1 if num == x else -1
        return x
