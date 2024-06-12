from typing import List

class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        pass

obj = Solution()
assert obj.longestAlternatingSubarray([3, 2, 5, 4], 5) == 3
assert obj.longestAlternatingSubarray([1, 2], 2) == 1
assert obj.longestAlternatingSubarray([2, 3, 4, 5], 4) == 3
