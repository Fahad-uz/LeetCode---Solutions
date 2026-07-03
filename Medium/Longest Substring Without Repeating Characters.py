class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        j=0
        longest=0
        characters=set()
        while(j<len(s)):
            if s[j] in characters:
                characters.remove(s[i])
                i+=1
            else:
                characters.add(s[j])
                window=j-i+1
                longest=max(longest,window)
                j+=1
        return longest
                
