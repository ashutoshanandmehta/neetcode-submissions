class Solution:
    def solve(self, nums: List[int],memo,n:int)-> int:
        if n==0:
            return 0
        if n==1:
            return nums[0]
        if n in memo:
            return memo[n]
        memo[n]=max(self.solve(nums,memo,n-1),nums[n-1]+self.solve(nums,memo,n-2))
        return memo[n]

    def rob(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        
        memo={}
        return self.solve(nums,memo,len(nums))
    
