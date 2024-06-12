from typing import List

class Solution:
    def maxPalindromesAfterOperations(self, words: List[str]) -> int:
        pass

obj = Solution()
assert obj.maxPalindromesAfterOperations(["abbb", "ba", "aa"]) == 3
assert obj.maxPalindromesAfterOperations(["abc", "ab"]) == 2
assert obj.maxPalindromesAfterOperations(["cd", "ef", "a"]) == 1
