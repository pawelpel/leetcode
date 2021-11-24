# https://leetcode.com/problems/two-sum/
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        _nums = sorted(nums)

        start, stop = 0, len(_nums)-1

        while 1:
            current_sum = _nums[start] + _nums[stop]

            if current_sum == target:
                break
            if current_sum < target:
                start += 1
            if current_sum > target:
                stop -= 1

        start, stop = sorted([start, stop])

        x = nums.index(_nums[start])
        nums[x] = None  # avoid finding the same index
        y = nums.index(_nums[stop])
        return [x, y]


s = Solution()
assert s.twoSum([2, 7, 11, 15], 9) == [0, 1]
assert s.twoSum([3, 2, 4], 6) == [1, 2]
assert s.twoSum([3, 3], 6) == [0, 1]
assert s.twoSum([-3, 4, 3, 90], 0) == [0, 2]
assert sorted(s.twoSum([5, 75, 25], 100)) == [1, 2]
