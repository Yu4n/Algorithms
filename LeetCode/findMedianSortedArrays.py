def findMedianSortedArrays(nums1, nums2) -> float:
    nums1.extend(nums2)
    list.sort(nums1)
    n = len(nums1)
    return (nums1[n // 2 - 1] + nums1[n // 2]) / 2 if n % 2 == 0 else nums1[n // 2]
