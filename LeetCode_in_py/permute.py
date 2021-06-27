class Solution:
    def __init__(self):
        self.res = []

    def permute(self, nums: [int]) -> [[int]]:
        track = []
        self.backtrack(nums, track)
        return self.res

    def backtrack(self, nums, track):
        if len(nums) == len(track):
            self.res.append(track[:])  # deep copy track and append
            print(self.res)
            return
        for i in range(len(nums)):
            if nums[i] in track:
                continue
            track.append(nums[i])
            self.backtrack(nums, track)
            track.pop()
