import math

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d={}
        #edge cases
        if len(nums)==0:
            return 0

        #storing the numbers in hashmap
        for x in nums:
            d[x]=x

        d2={}
        # getting the starting of the sequence
        for x in d:
            if x-1 not in d and x+1 in d:
                d2[x]=x
            
        #checking longest subsequence
        count=1
        for x in d2:
            n=x
            count2=1
            while(n+1 in d):
                n=n+1
                count2=count2+1
            if count2>count:
                count=count2
        return count


            
            


        