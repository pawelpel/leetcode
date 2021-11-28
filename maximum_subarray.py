# https://leetcode.com/problems/maximum-subarray/
from math import inf
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ret_sum = -inf
        curr_sum = 0

        for i in range(len(nums)):
            curr_sum = curr_sum + nums[i]

            if curr_sum > ret_sum:
                ret_sum = curr_sum

            if curr_sum < 0:
                curr_sum = 0

            print(i, curr_sum, ret_sum)
        return ret_sum


s = Solution()
assert s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
assert s.maxSubArray([1]) == 11
assert s.maxSubArray([5, 4, -1, 7, 8]) == 23
assert s.maxSubArray([-1, -1, 2, -1, -1]) == 2
assert s.maxSubArray([-1, -1, 1, 2, 3, -1]) == 6
assert s.maxSubArray([1, -1, -1, -1, 100]) == 100
assert s.maxSubArray([-1]) == -1
assert s.maxSubArray([-1, -2, -3, 0, -2, -1]) == 0
assert s.maxSubArray([-1, -2, -3, 0, -3, -2, -1]) == 0
assert s.maxSubArray([31, -41, 59, 26, -53, 58, 97, -93, -23, 84]) == 187
assert s.maxSubArray([-1, -2, -3, -1, -2, -3]) == -1
assert s.maxSubArray([0]) == 0
