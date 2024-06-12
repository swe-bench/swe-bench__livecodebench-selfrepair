from typing import List

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        pass

obj = Solution()
assert obj.countServers(3, [[1, 3], [2, 6], [1, 5]], 5, [10, 11]) == [1, 2]
assert obj.countServers(3, [[2, 4], [2, 1], [1, 2], [3, 1]], 2, [3, 4]) == [0, 1]
