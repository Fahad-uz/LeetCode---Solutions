class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        maxx=0
        d={}
        kk=0
        res=[]
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        while (k>0):
            for key,value in d.items():
                if value>maxx:
                    maxx=value
                    kk=key
            del d[kk]
            res.append(kk)
            k-=1
            maxx=0
        return res
