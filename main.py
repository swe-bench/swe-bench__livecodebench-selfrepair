from typing import List

class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        pass

obj = Solution()
assert obj.longestValidSubstring("cbaaaabc", ["aaa", "cb"]) == 4
assert obj.longestValidSubstring("leetcode", ["de", "le", "e"]) == 4
