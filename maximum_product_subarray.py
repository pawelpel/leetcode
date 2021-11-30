# https://leetcode.com/problems/maximum-product-subarray/
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums_len = len(nums)

        max_so_far = nums[0]
        max_end = min_end = max_so_far

        for i in range(1, nums_len):
            temp = max_end

            n = nums[i]

            max_end = max(n, n * temp, n * min_end)
            min_end = min(n, n * temp, n * min_end)

            max_so_far = max(max_so_far, max_end, min_end)

        return max_so_far


s = Solution()
assert s.maxProduct([2, 3, -2, 4]) == 6
assert s.maxProduct([-2, 0, -1]) == 0
assert s.maxProduct([-3, -1, -1]) == 3
assert s.maxProduct([0]) == 0
assert s.maxProduct([0, 2]) == 2
assert s.maxProduct([3, -1, 4]) == 4
assert s.maxProduct([10, -1, -1, -9]) == 10
assert s.maxProduct([-2, 3, -4]) == 24
assert s.maxProduct([2, -5, -2, -4, 3]) == 24
