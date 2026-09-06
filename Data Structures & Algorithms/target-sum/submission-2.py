class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        s=sum(nums)
        new_sum=(target+s)/2
        memo={}
        return self.solve(nums,new_sum,len(nums),memo)
        
    def solve(self,nums:List[int],target,n: int, memo:List[int]):
        if n==0:
            if target==0:
                return 1
            return 0
        if (n,target) in memo:
            return memo[(n,target)]
        dont_take=self.solve(nums,target,n-1,memo)
        
        take=0
        if nums[n-1]<=target:
            take=self.solve(nums,(target-nums[n-1]),n-1,memo)
        memo[(n,target)]=dont_take+take

        return memo[(n,target)]
