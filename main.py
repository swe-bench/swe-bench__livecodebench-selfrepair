from typing import List

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        pass

obj = Solution()
assert obj.countPrefixSuffixPairs(["a", "aba", "ababa", "aa"]) == 4
assert obj.countPrefixSuffixPairs(["pa", "papa", "ma", "mama"]) == 2
assert obj.countPrefixSuffixPairs(["abab", "ab"]) == 0
