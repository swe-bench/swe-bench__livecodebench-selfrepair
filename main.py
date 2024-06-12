from typing import List

class Solution:
    def minOperations(self, nums: List[int], target: int) -> int:
        pass

obj = Solution()
assert obj.minOperations([1, 2, 8], 7) == 1
assert obj.minOperations([1, 32, 1, 2], 12) == 2
assert obj.minOperations([1, 32, 1], 35) == -1
