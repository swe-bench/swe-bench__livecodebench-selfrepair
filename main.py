from typing import List

class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        pass

obj = Solution()
assert obj.lengthOfLongestSubsequence([1, 2, 3, 4, 5], 9) == 3
assert obj.lengthOfLongestSubsequence([4, 1, 3, 2, 1, 5], 7) == 4
assert obj.lengthOfLongestSubsequence([1, 1, 5, 4, 5], 3) == -1
