class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights)-1
        s=0
        while left<right:
            temp=min(heights[left],heights[right])*(right-left)
            if temp>s:
                s=temp
            if heights[left]<heights[right]:
                left=left+1
            else:
                right=right-1
        return s
        