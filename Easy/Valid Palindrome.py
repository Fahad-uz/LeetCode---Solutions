class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        st=""
        s=s.lower()
        for i in s:
            if i.isalnum():
                st+=i
            else:
                continue
        if st==st[::-1]:
            return True
        else:
            return False  
