class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo={}
        ind=len(coins)
        ans=self.solve(coins,amount,ind,memo)
        if ans>=1e8:
            return -1
        return ans
    
    def solve(self, coins: List[int], amount,n: int, memo: dict)-> int:
        if n==0 and amount!=0:
            if amount%coins[0]==0:
                return amount//coins[0]
            else:
                return 1e8
        if amount==0:
            return 0
        if (n,amount) in memo:
             return memo[(n,amount)]

        dont_take=self.solve(coins,amount,n-1,memo)
        take=1e8

        if coins[n-1]<=amount:
            take=self.solve(coins,amount-coins[n-1],n,memo)+1
        memo[(n,amount)]=min(dont_take,take)

        return memo[(n,amount)]
        

        