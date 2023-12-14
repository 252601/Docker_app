
import numpy as np
import bisect


class Solution:
    def merge(self, arr1, m: int, arr2, n: int) -> None:
        arr1.sort()
        arr1.resize(m+n, refcheck=True)
        print(arr1)
        for i in arr2:
            print(i)
            position = np.searchsorted(nums1, i)
            print(position)
            arr1 = np.insert(arr1, [position], i)
        print(arr1)


nums1 = np.array([3,2,1])
nums2 = np.array([2,4,5])
prob = Solution()
prob.merge(nums1, len(nums1), nums2, len(nums2))




# merge(nums1,nums2)
