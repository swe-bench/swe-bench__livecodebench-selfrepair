from typing import List

class Solution:
    def countSubMultisets(self, nums: List[int], l: int, r: int) -> int:
        pass

obj = Solution()
assert obj.countSubMultisets([1, 2, 2, 3], 6, 6) == 1
assert obj.countSubMultisets([2, 1, 4, 2, 7], 1, 5) == 7
assert obj.countSubMultisets([1, 2, 1, 3, 5, 2], 3, 5) == 9
