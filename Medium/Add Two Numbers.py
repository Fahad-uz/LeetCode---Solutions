# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c1=l1
        c2=l2
        test1=[]
        test2=[]
        while c1 is not None:
            test1.append(c1.val)
            c1=c1.next
        while c2 is not None:
            test2.append(c2.val)
            c2=c2.next
        test1.reverse()
        test2.reverse()
        res1=int("".join(map(str,test1)))
        res2=int("".join(map(str,test2)))
        sum=res1+res2
        t=[int(digit) for digit in str(sum)]
        t.reverse()
        result=ListNode()
        dummy=result
        for i in t:
            dummy.next=ListNode(i)
            dummy=dummy.next
        return result.next
