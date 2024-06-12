class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        pass

obj = Solution()
assert obj.minimumTimeToInitialState("abacaba", 3) == 2
assert obj.minimumTimeToInitialState("abacaba", 4) == 1
assert obj.minimumTimeToInitialState("abcbabcd", 2) == 4
