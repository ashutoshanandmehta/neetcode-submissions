class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        t={}
        n=len(cost)
        if n==0:
            return 0
        memo={}
        return self.solve(cost,n, memo)
    
    def solve(self, cost: List[int], n:int, memo)->int:
        if n<=1:
            return 0
        if n in memo:
            return memo[n]
        else:
            memo[n]=min(self.solve(cost,n-1,memo)+cost[n-1],self.solve(cost,n-2,memo)+cost[n-2])
        return memo[n]

        