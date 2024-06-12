from typing import List

class Solution:
    def minimizeConcatenatedLength(self, words: List[str]) -> int:
        pass

obj = Solution()
assert obj.minimizeConcatenatedLength(["aa", "ab", "bc"]) == 4
assert obj.minimizeConcatenatedLength(["ab", "b"]) == 2
assert obj.minimizeConcatenatedLength(["aaa", "c", "aba"]) == 6
