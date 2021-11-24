# https://leetcode.com/problems/product-of-array-except-self/
import functools
import operator
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        cache = {}

        def calculate_or_cached(idx: int):
            value = nums[idx]
            if cached := cache.get(value):
                return cached

            cache[value] = functools.reduce(operator.mul, nums[:idx]+nums[idx+1:])
            return cache[value]

        return [calculate_or_cached(x) for x in range(len(nums))]


s = Solution()
assert s.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
assert s.productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
