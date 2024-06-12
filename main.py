from typing import List

class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        pass

obj = Solution()
assert obj.maxNonDecreasingLength([2, 3, 1], [1, 2, 1]) == 2
assert obj.maxNonDecreasingLength([1, 3, 2, 1], [2, 2, 3, 4]) == 4
assert obj.maxNonDecreasingLength([1, 1], [2, 2]) == 2
