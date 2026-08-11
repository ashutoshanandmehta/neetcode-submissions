class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for x in nums:
            key = x
            if key not in d:
                d[key]=0

            d[key]=d[key] +1
        
        sorted_d = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))

        return list(sorted_d.keys())[:k]
