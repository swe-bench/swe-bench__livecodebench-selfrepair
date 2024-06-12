from typing import List

class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        pass

obj = Solution()
assert obj.relocateMarbles([1, 6, 7, 8], [1, 7, 2], [2, 9, 5]) == [5, 6, 8, 9]
assert obj.relocateMarbles([1, 1, 3, 3], [1, 3], [2, 2]) == [2]
