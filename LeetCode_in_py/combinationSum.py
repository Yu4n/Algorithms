class Solution:
    def combinationSum(self, candidates, target):
        ret = []
        self.dfs(candidates, target, [], ret)
        return ret

    def dfs(self, nums, target, path, ret):
        if target < 0:
            return
        if target == 0:
            ret.append(path)
            return
        for i in range(len(nums)):
            self.dfs(nums[i:], target - nums[i], path + [nums[i]], ret)

    def combinationSum_(self, candidates, target):
        ans = []
        N = len(candidates)
        candidates.sort()

        def backtrack(start, combination, cusum):
            if cusum > 500:
                return
            if cusum == target:
                ans.append(combination[:])
                return
            for i in range(start, N):
                if cusum + candidates[i] > target:
                    return
                combination.append(candidates[i])
                backtrack(i, combination, cusum + candidates[i])
                combination.pop()

        backtrack(0, [], 0)
        return ans

    def combinationSumDP(self, candidates, target):
        dp = {i: [] for i in range(target + 1)}
        # 这里一定要将candidates降序排列
        for i in sorted(candidates, reverse=True):
            for j in range(i, target + 1):
                if j == i:
                    dp[j] = [[i]]
                else:
                    dp[j].extend([x + [i] for x in dp[j - i]])
        return dp[target]
