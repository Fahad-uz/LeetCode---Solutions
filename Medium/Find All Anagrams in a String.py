from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p)>len(s):
            return []
        i=0
        j=len(p)
        l=[]
        p_count=Counter(p)
        window_count=Counter(s[i:j])
        while(j<=len(s)):
            if p_count==window_count:
                l.append(i)
            if j == len(s):
                break
            window_count[s[i]]-=1
            window_count[s[j]]+=1
            i+=1
            j+=1
        return l
