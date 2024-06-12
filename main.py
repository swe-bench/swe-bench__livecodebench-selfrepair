from typing import List

class Solution:
    def maximumSumQueries(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        pass

obj = Solution()
assert obj.maximumSumQueries([4, 3, 1, 2], [2, 4, 9, 5], [[4, 1], [1, 3], [2, 5]]) == [6, 10, 7]
assert obj.maximumSumQueries([3, 2, 5], [2, 3, 4], [[4, 4], [3, 2], [1, 1]]) == [9, 9, 9]
assert obj.maximumSumQueries([2, 1], [2, 3], [[3, 3]]) == [-1]
