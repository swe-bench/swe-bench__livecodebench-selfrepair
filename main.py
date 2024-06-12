from typing import List

class Solution:
    def lastVisitedIntegers(self, words: List[str]) -> List[int]:
        pass

obj = Solution()
assert obj.lastVisitedIntegers(["1", "2", "prev", "prev", "prev"]) == [2, 1, -1]
assert obj.lastVisitedIntegers(["1", "prev", "2", "prev", "prev"]) == [1, 2, 1]
