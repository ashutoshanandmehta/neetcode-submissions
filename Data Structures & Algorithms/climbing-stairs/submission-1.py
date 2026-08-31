class Solution:
        
    def solve(self,n:int, memo):
        if (n<=2):
            return n
        if n in memo:
            return memo[n]
        else:
            memo[n]=self.solve(n-1,memo)+self.solve(n-2,memo)
        return memo[n]


    def climbStairs(self, n: int) -> int:
        memo={}
        return self.solve(n,memo)


        