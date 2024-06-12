from typing import List

class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        pass

obj = Solution()
assert obj.minSizeSubarray([1, 2, 3], 5) == 2
assert obj.minSizeSubarray([1, 1, 1, 2, 3], 4) == 2
assert obj.minSizeSubarray([2, 4, 6, 8], 3) == -1
