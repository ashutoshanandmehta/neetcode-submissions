class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        memo1={}
        memo2={}
        return max(
            self.rob_linear(nums[:-1],(len(nums)-1),memo1), 
            self.rob_linear(nums[1:],(len(nums)-1),memo2)    
        )

    def rob_linear(self, nums: List[int], n: int, memo) -> int:
        if n==0:
            return 0
        if n==1:
            return nums[0]
        if n in memo:
            return memo[n]
        memo[n]=max(self.rob_linear(nums, n-1, memo),nums[n-1]+self.rob_linear(nums,n-2,memo))
        return memo[n]



        