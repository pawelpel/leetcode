# https://leetcode.com/problems/bulb-switcher-iii/
from typing import List


class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        turned_on = max_bulb = moments = 0

        for l in light:
            turned_on += 1

            if l > max_bulb:
                max_bulb = l

            if max_bulb == turned_on:
                moments += 1

        return moments
