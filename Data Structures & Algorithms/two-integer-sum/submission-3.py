class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i in range(0,len(nums)):
            for j in range(i,len(nums)):
                if(target == nums[i]+nums[j] and i!=j):
                    return [i,j]