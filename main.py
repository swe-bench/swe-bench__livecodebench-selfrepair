from typing import List

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        pass

obj = Solution()
assert obj.maximumNumberOfStringPairs(["cd", "ac", "dc", "ca", "zz"]) == 2
assert obj.maximumNumberOfStringPairs(["ab", "ba", "cc"]) == 1
assert obj.maximumNumberOfStringPairs(["aa", "ab"]) == 0
