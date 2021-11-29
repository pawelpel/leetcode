# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # return min(nums)

        n_len = len(nums)

        start = 0
        stop = n_len - 1

        if n_len == 1:
            return nums[0]

        while 1:
            middle = (start + stop) // 2

            if middle + 1 > n_len:
                return nums[middle]

            if nums[middle] > nums[middle + 1]:
                return nums[middle + 1]

            if nums[start] > nums[middle]:
                stop = middle
                continue

            if nums[middle] > nums[stop]:
                start = middle
                continue

            return nums[0]


s = Solution()
assert s.findMin([1]) == 1
assert s.findMin([1, 2]) == 1
assert s.findMin([1, 2, 3, 4, 5, 6]) == 1
assert s.findMin([2, 3, 4, 5, 6, 0, 1]) == 0
assert s.findMin([1, 2, 3]) == 1
assert s.findMin([3, 2, 1]) == 1
assert s.findMin([3, 4, 5, 1, 2]) == 1
assert s.findMin([4, 5, 6, 7, 0, 1, 2, 3]) == 0
assert s.findMin([11, 13, 15, 17]) == 11
