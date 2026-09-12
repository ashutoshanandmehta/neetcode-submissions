class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum=0
        for i in range(len(prices)-1):
            for j in range(i+1,len(prices)):
                profit=prices[j]-prices[i]
                if profit<0:
                    profit=0
                minimum=max(minimum,profit)


        return minimum

        