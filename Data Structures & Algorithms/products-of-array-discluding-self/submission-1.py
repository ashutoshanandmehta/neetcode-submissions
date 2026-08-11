class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        d={}
        d[0]=0
        out=[]
        for x in nums:
            if x == 0:
                d[0]=d[0]+1

        if d[0]==1:
            out=[0]*len(nums)
            result=1
            mark=0
            for i in range(0,len(nums)):
                if nums[i] == 0:
                    mark=i
                    continue
                else:
                    result=result*nums[i]
            out[mark]=result
            return out


        if d[0]>1:
            out=[0]*len(nums)
            return out

        else:
            out=[0]*len(nums)
            result=1
            for x in range(0,len(nums)):
                result=result*nums[x]
            for x in range(0, len(nums)):
                out[x]=int(result/nums[x])
            return out