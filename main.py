from typing import List

class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        pass

obj = Solution()
assert obj.maximumJumps([1, 3, 6, 4, 1, 2], 2) == 3
assert obj.maximumJumps([1, 3, 6, 4, 1, 2], 3) == 5
assert obj.maximumJumps([1, 3, 6, 4, 1, 2], 0) == -1
