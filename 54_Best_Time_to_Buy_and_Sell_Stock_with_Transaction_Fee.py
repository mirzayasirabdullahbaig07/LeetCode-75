class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        buy = 0
        sell = 0
        buy = -prices[0]
        
        for i in range(1, n):
            buy2 = max(buy, sell - prices[i])
            sell2 = max(sell, buy + prices[i] - fee)
            buy = buy2
            sell = sell2
            
        return sell