from typing import List

class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        pass

obj = Solution()
assert obj.getGoodIndices([[2, 3, 3, 10], [3, 3, 3, 1], [6, 1, 1, 4]], 2) == [0, 2]
assert obj.getGoodIndices([[39, 3, 1000, 1000]], 17) == []
