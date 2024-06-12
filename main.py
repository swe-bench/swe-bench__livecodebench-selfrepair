from typing import List

class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        pass

obj = Solution()
assert obj.countMatchingSubarrays([1, 2, 3, 4, 5, 6], [1, 1]) == 4
assert obj.countMatchingSubarrays([1, 4, 4, 1, 3, 5, 5, 3], [1, 0, -1]) == 2
