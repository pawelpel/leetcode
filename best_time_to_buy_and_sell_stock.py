# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_value = prices[0]
        max_value = prices[0]
        max_profit = 0
        for p in prices:
            if p < min_value:
                min_value = max_value = p
            if p > max_value:
                max_value = p
            current_profit = max_value - min_value
            if current_profit > max_profit:
                max_profit = current_profit
        return max_profit


s = Solution()
assert s.maxProfit([7, 1, 5, 3, 6, 4]) == 5
assert s.maxProfit([7, 6, 4, 3, 1]) == 0
assert s.maxProfit([2, 4, 1]) == 2
assert s.maxProfit([1, 2]) == 1

