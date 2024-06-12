from typing import List

class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        pass

obj = Solution()
assert obj.isAcronym(["alice", "bob", "charlie"], "abc") == True
assert obj.isAcronym(["an", "apple"], "a") == False
assert obj.isAcronym(["never", "gonna", "give", "up", "on", "you"], "ngguoy") == True
