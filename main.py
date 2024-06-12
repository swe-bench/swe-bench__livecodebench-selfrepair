from typing import List

class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        pass

obj = Solution()
assert obj.earliestSecondToMarkIndices([2, 2, 0], [2, 2, 2, 2, 3, 2, 2, 1]) == 8
assert obj.earliestSecondToMarkIndices([1, 3], [1, 1, 1, 2, 1, 1, 1]) == 6
assert obj.earliestSecondToMarkIndices([0, 1], [2, 2, 2]) == -1
