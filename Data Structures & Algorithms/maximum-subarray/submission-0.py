class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        current_sum=nums[0]
        global_sum=nums[0]
        for i in range(1, len(nums)):
            current_sum=max(nums[i],nums[i]+current_sum)
            global_sum=max(global_sum,current_sum)

        return global_sum