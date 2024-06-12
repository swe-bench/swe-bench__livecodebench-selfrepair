from typing import List

class Solution:
    def canMakePalindromeQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        pass

obj = Solution()
assert obj.canMakePalindromeQueries("abcabc", [[1, 1, 3, 5], [0, 2, 5, 5]]) == [True, True]
assert obj.canMakePalindromeQueries("abbcdecbba", [[0, 2, 7, 9]]) == [False]
assert obj.canMakePalindromeQueries("acbcab", [[1, 2, 4, 5]]) == [True]
