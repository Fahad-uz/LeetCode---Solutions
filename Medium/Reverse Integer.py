class Solution:
    def reverse(self, x: int) -> int:
        sign= -1 if x<0 else 1
        reversed_integer=int(str(abs(x))[::-1])
        rev=sign*reversed_integer
        if rev<=2147483647 and rev>=-2147483647:
            return rev
        else:
            return 0
