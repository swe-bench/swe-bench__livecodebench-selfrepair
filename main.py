from typing import List

class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        pass

obj = Solution()
assert obj.constructProductMatrix([[1, 2], [3, 4]]) == [[24, 12], [8, 6]]
assert obj.constructProductMatrix([[12345], [2], [1]]) == [[2], [0], [0]]
