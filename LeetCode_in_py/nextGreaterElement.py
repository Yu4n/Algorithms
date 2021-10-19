from collections import deque


class Solution:
    def nextGreaterElement(self, nums1: [int], nums2: [int]) -> [int]:
        # 先遍历大数组nums2，首先将第一个元素入栈；
        # 继续遍历，当当前元素小于栈顶元素时，继续将它入栈；当当前元素大于栈顶元素时，栈顶元素出栈，此时应将该出栈的元素与当前元素形成key - value键值对，存入HashMap中；
        # 当遍历完nums2后，得到nums2中元素所对应的下一个更大元素的hash表；
        # 遍历nums1的元素在hashMap中去查找‘下一个更大元素’，当找不到时则为 - 1。
        hmap = {}
        stack = deque()

        for i in range(len(nums2)):
            while stack and stack[-1] < nums2[i]:
                hmap[stack.pop()] = nums2[i]
            stack.append(nums2[i])

        res = [-1] * len(nums1)
        for i in range(len(nums1)):
            if nums1[i] in hmap:
                res[i] = hmap[nums1[i]]
        return res


nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
sln = Solution()
print(sln.nextGreaterElement(nums1, nums2))
