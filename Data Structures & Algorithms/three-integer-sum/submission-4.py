from collections import Counter

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        hashmap = Counter(nums)
        start=nums[0]
        end=len(nums)
        output=[]
        for i in range(end):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,end):
          
                
                temp=[]
                target=-1*(nums[i]+nums[j])
                if target < nums[j]:
                    continue
                if target in hashmap:
                    value=hashmap[target]
                    if nums[i]==target:
                        value=value-1
                    if nums[j]==target:
                        value=value-1
                    if value>0:
                        if ([nums[i], nums[j], target]) not in output:
                            output.append([nums[i], nums[j], target])
        return output

