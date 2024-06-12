from typing import List

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        pass

obj = Solution()
assert obj.isGood([2, 1, 3]) == False
assert obj.isGood([1, 3, 3, 2]) == True
assert obj.isGood([1, 1]) == True
assert obj.isGood([3, 4, 4, 1, 2, 1]) == False
