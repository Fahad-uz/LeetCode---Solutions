class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        w=len(s1)
        i=0
        j=len(s1)
        while (j<=len(s2)):
            if sorted(s1)==sorted(s2[i:j]):
                return True
            else:
                i+=1
                j+=1
        return False
