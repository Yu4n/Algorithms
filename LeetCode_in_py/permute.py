class Solution:
    def permute(self, nums):
        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
            return
        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i + 1:], path + [nums[i]], res)


class Sln:
    def __init__(self):
        self.res = []

    def permute(self, nums: [int]) -> [[int]]:
        track = []
        self.backtrack(nums, track)
        return self.res

    def backtrack(self, nums, track):
        if len(nums) == len(track):  # if the condition is satisfied
            self.res.append(track[:])  # deep copy track and append
            print(self.res)
            return
        for i in range(len(nums)):
            if nums[i] in track:
                continue
            track.append(nums[i])  # decide
            self.backtrack(nums, track)
            track.pop()  # undo decision
