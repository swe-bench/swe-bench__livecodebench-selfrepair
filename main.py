from typing import List

class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        pass

obj = Solution()
assert obj.colorTheArray(4, [[0, 2], [1, 2], [3, 1], [1, 1], [2, 1]]) == [0, 1, 1, 0, 2]
assert obj.colorTheArray(1, [[0, 100000]]) == [0]
