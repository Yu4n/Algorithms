class Solution:
    def nextGreaterElement(self, nums1: [int], nums2: [int]) -> [int]:
        dct = {}
        res = []
        n = len(nums2)
        for num in nums1:
            dct[num] = nums2.index(num)
        for key in dct.keys():
            if dct[key] + 1 == n:
                res.append(-1)
                continue
            for i in range(dct[key] + 1, n):
                if nums2[i] > key:
                    res.append(nums2[i])
                    break
                if i == n - 1 and nums2[i] <= key:
                    res.append(-1)
                    break
        return res


nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
sln = Solution()
print(sln.nextGreaterElement(nums1, nums2))
