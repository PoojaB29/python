class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices)==0 or k == 0:
            return 0
        t = len(prices)/2
        if k >= t:
            #many transactions
            p=0
            for i in range(1,len(prices)):
                if prices[i] > prices[i-1]:
                    p = p + prices[i] - prices[i-1]
            return p
        # 1 transactions
        minimum = prices[0]
        p=0
        profit = [0]* len(prices)
        for i in range(len(prices)):
            minimum = min(minimum, prices[i])
            p = max(p, prices[i] - minimum)
            profit[i] = p
        # k-1 transactions
        for i in range(1,k):
            self.ktimes(prices, profit)
        ans = 0
        for i in range (len(profit)):
            ans = max (profit[i], ans)
        return ans
    
    def ktimes(self, prices, profit):
        p2 = 0
        b2 = float('inf')
        for i in range(len(prices)):
            b2 = min (b2, prices[i] -profit[i] )
            p2 = max (p2 , prices[i] - b2)
            profit[i] = p2
            