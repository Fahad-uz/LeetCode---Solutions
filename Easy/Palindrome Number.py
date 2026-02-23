class Solution:
    def isPalindrome(self, x: int) -> bool:
        org=x
        rev=0
        while(org>0):
            temp=org%10
            rev=rev*10+temp
            org=org//10
        if x==rev:
            return True
        return False
