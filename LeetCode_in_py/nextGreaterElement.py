class Solution:
    def nextGreaterElement(self, nums1: [int], nums2: [int]) -> [int]:
        greater_map = {x: -1 for x in nums1}
        stack = []

        for num in nums2:
            while stack and stack[-1] < num:
                prev_num = stack.pop()
                if prev_num in greater_map:
                    greater_map[prev_num] = num
            stack.append(num)

        return [greater_map[x] for x in nums1]


nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
sln = Solution()
print(sln.nextGreaterElement(nums1, nums2))
