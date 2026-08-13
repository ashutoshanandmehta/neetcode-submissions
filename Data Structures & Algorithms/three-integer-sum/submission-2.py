class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        left=0
        result=[]
        right=len(nums)-1
        while left<right-1:
            middle=left+1
            target=nums[left]*(-1)
            while middle<right:
                temp=[]
                s=nums[right]+nums[middle]
                if s==target:
                    temp.append(nums[left])
                    temp.append(nums[middle])
                    temp.append(nums[right])
                    if temp not in result:
                        result.append(temp)
                if s<target:
                    middle=middle+1
                else:
                    right=right-1
            
            left=left+1
            right=len(nums)-1
        return result
             

        