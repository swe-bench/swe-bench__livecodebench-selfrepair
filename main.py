from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        pass

obj = Solution()
assert obj.findWordsContaining(["leet", "code"], "e") == [0, 1]
assert obj.findWordsContaining(["abc", "bcd", "aaaa", "cbc"], "a") == [0, 2]
assert obj.findWordsContaining(["abc", "bcd", "aaaa", "cbc"], "z") == []
