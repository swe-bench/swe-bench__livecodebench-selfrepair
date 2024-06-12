from typing import List

class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        pass

obj = Solution()
assert obj.distinctDifferenceArray([1, 2, 3, 4, 5]) == [-3, -1, 1, 3, 5]
assert obj.distinctDifferenceArray([3, 2, 3, 4, 2]) == [-2, -1, 0, 2, 3]
