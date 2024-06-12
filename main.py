from typing import List

class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        pass

obj = Solution()
assert obj.splitWordsBySeparator(["one.two.three", "four.five", "six"], ".") == ["one", "two", "three", "four", "five", "six"]
assert obj.splitWordsBySeparator(["$easy$", "$problem$"], "$") == ["easy", "problem"]
assert obj.splitWordsBySeparator(["|||"], "|") == []
