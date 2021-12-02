# https://leetcode.com/problems/search-in-rotated-sorted-array/
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n_len = len(nums)

        str.isalnum()
        if n_len == 1:
            return 0 if target == nums[0] else -1

        def find_minimum():
            start = 0
            stop = n_len - 1

            while 1:
                middle = (start + stop) // 2

                if middle + 1 > n_len:
                    return middle

                if nums[middle] > nums[middle + 1]:
                    return middle + 1

                if nums[start] > nums[middle]:
                    stop = middle
                    continue

                if nums[middle] > nums[stop]:
                    start = middle
                    continue

                return 0

        minimum_idx = find_minimum()
        minimum = nums[minimum_idx]

        if minimum == target:
            return minimum_idx

        max_value = nums[minimum_idx - 1]

        if target > max_value or target < minimum:
            return -1

        if minimum_idx == 0:
            return target - minimum

        right_idx = n_len - 1
        right = nums[right_idx]

        offset = 0
        if target <= right:
            offset = minimum_idx

        return target - minimum + offset


s = Solution()
assert s.search([4, 5, 6, 7, 0, 1, 2], 0) == 4
assert s.search([4, 5, 6, 7, 0, 1, 2], 3) == -1
assert s.search([4, 5, 6, 7], 4) == 0
assert s.search([3, 4, 5, 6, 7], 4) == 1
assert s.search([1], 0) == -1
