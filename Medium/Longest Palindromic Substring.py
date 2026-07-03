class Solution:
    def longestPalindrome(self, s: str) -> str:
        l=""
        for i in range(len(s)):
            for j in range(i,len(s)):
                current=s[i:j+1]
                if current==current[::-1]:
                    if len(current)>len(l):
                        l=current
        return l
