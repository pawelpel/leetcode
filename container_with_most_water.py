# https://leetcode.com/problems/container-with-most-water/
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0

        start, stop = 0, len(height) - 1

        while start < stop:
            left_wall = height[start]
            right_wall = height[stop]

            curr_area = min(left_wall, right_wall) * (stop - start)
            max_area = max(max_area, curr_area)

            if left_wall < right_wall:
                start += 1
            else:
                stop -= 1

        return max_area


s = Solution()
assert s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
assert s.maxArea([1, 1]) == 1
assert s.maxArea([4, 3, 2, 1, 4]) == 16
assert s.maxArea([1, 2, 1, 2]) == 4
assert s.maxArea([1, 2, 1]) == 2
assert s.maxArea([2, 3, 4, 5, 18, 17, 6]) == 17
assert s.maxArea([1, 3, 2, 5, 25, 24, 5]) == 24
assert s.maxArea([4, 6, 4, 4, 6, 2, 6, 7, 11, 2]) == 42
assert s.maxArea(
    [76, 155, 15, 188, 180, 154, 84, 34, 187, 142, 22, 5, 27, 183, 111, 128, 50, 58, 2, 112, 179, 2, 100, 111, 115, 76,
     134, 120, 118, 103, 31, 146, 58, 198, 134, 38, 104, 170, 25, 92, 112, 199, 49, 140, 135, 160, 20, 185, 171, 23, 98,
     150, 177, 198, 61, 92, 26, 147, 164, 144, 51, 196, 42, 109, 194, 177, 100, 99, 99, 125, 143, 12, 76, 192, 152, 11,
     152, 124, 197, 123, 147, 95, 73, 124, 45, 86, 168, 24, 34, 133, 120, 85, 81, 163, 146, 75, 92, 198, 126, 191]
) == 18048
