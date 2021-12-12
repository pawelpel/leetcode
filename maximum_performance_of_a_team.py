# https://leetcode.com/problems/maximum-performance-of-a-team/
from heapq import heappop, heappush, heapify
from typing import List


class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        speed_to_reliability = sorted(
            zip(speed, efficiency),
            key=lambda x: x[1],
            reverse=True,
        )

        maximum = 0
        total_speed = 0
        h = []
        heapify(h)

        for sr in speed_to_reliability:
            spe = sr[0]  # speed
            eff = sr[1]  # efficiency

            if len(h) < k:
                total_speed += spe
                heappush(h, spe)
                maximum = max(maximum, eff * total_speed)
            else:
                smallest_speed = heappop(h)
                total_speed -= smallest_speed
                total_speed += spe
                heappush(h, spe)
                maximum = max(maximum, eff * total_speed)

        return maximum % (10 ** 9 + 7)


s = Solution()
assert s.maxPerformance(n=6, speed=[2, 10, 3, 1, 5, 8], efficiency=[5, 4, 3, 9, 7, 2], k=2) == 60
