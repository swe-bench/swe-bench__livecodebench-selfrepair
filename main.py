from typing import List

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        pass

obj = Solution()
assert obj.maximumSubarraySum([1, 2, 3, 4, 5, 6], 1) == 11
assert obj.maximumSubarraySum([-1, 3, 2, 4, 5], 3) == 11
assert obj.maximumSubarraySum([-1, -2, -3, -4], 2) == -6
