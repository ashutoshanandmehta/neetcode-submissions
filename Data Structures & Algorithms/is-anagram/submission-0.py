class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d={}
        k={}
        for i in s:
            d[i]=d.get(i,0)+1

        for i in t:
            k[i]=k.get(i,0)+1
            
        if d==k:
            return True
        else:
            return False