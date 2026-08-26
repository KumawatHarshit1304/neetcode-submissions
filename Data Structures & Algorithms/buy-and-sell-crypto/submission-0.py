class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_p = prices[0]
        max_prof = 0

        for i in range(1,len(prices)):
            if prices[i] < min_p:
                min_p = prices[i]
            else:
                profit = prices[i] - min_p

                max_prof = max(profit,max_prof)
        return max_prof
        