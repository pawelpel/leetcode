# https://leetcode.com/problems/maximum-product-subarray/
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_product = ret_product = nums[0]

        for i in range(1, len(nums)):

            new_product = curr_product * nums[i]
            print(i, new_product, curr_product, ret_product)

            if new_product > curr_product or i+1 < len(nums) and new_product * nums[i+1] > curr_product:
                curr_product = new_product
            else:
                curr_product = nums[i]

            if curr_product > ret_product:
                ret_product = curr_product

        return ret_product



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
