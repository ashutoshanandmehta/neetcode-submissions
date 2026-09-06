class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1)==0 or len(text2)==0:
            return 0
        n1=len(text1)
        n2=len(text2)
        memo={}
        return self.solve(text1,text2,n1-1,n2-1,memo)
    def solve(self,text1: str, text2: str,n1: int, n2: int,memo:dict) -> int:
        if n1<0 or n2<0:
            return 0
        if (n1,n2) in memo:
            return memo[(n1,n2)]
        if text1[n1]==text2[n2]:
            memo[(n1,n2)]= (1+ self.solve(text1,text2,n1-1,n2-1,memo))
            return memo[(n1,n2)]
        else:
            memo[(n1,n2)]=max(self.solve(text1,text2,n1-1,n2,memo), self.solve(text1,text2,n1,n2-1,memo))
        return memo[(n1,n2)]
         

        
        
        