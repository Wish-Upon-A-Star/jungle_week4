# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        upnum=0
        iend=0
        jend=0
        ret=ListNode()
        i=l1
        j=l2
        print(i.val,j.val,ret)
        while (jend==0 and iend==0) or ((iend==0 or jend==0) and upnum==1):
            now=0
            if iend==0:
                now+=i.val
            if jend==0:
                now+=j.val
            now+=upnum
            print(now)
            print(upnum)
            ret.val=now%10
            ret.next=ListNode()
            upnum=now//10


            if i.next!=None:
                i=i.next
            else:
                iend=1
            if j.next!=None:
                j=j.next
            else:
                jend=1
        return ret