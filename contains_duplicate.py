# https://leetcode.com/problems/contains-duplicate/submissions/
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)


s = Solution()
assert s.containsDuplicate([1, 2, 3, 4]) is False
