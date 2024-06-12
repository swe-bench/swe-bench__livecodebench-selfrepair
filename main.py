from typing import List

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        pass

obj = Solution()
assert obj.maxSubarrayLength([1, 2, 3, 1, 2, 3, 1, 2], 2) == 6
assert obj.maxSubarrayLength([1, 2, 1, 2, 1, 2, 1, 2], 1) == 2
assert obj.maxSubarrayLength([5, 5, 5, 5, 5, 5, 5], 4) == 4
