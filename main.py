from typing import List

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        pass

obj = Solution()
assert obj.minimumCost("abcd", "acbe", ["a", "b", "c", "c", "e", "d"], ["b", "c", "b", "e", "b", "e"], [2, 5, 5, 1, 2, 20]) == 28
assert obj.minimumCost("aaaa", "bbbb", ["a", "c"], ["c", "b"], [1, 2]) == 12
assert obj.minimumCost("abcd", "abce", ["a"], ["e"], [10000]) == -1
