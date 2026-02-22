class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_buy = prices[0]
        for i in range(1, len(prices)):
            possible_profit = max(prices[i:]) - min_buy
            if(possible_profit > max_profit):
                max_profit= possible_profit
            min_buy = prices[i]
        return max_profit
            