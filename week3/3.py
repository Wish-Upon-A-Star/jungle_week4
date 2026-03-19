# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr=[]
        while head.next!=None:
            arr.append(head.val)
            head=head.next
        arr=self.mergesort(arr)
        rets=ListNode()
        ret=rets
        for i in arr:
            ret.val=i
            ret.next=ListNode()
            ret=ret.next
        return rets

        
    
    def mergesort(self,arr):
        retar=[]
        if len(arr)==1:
            return arr
        larr=self.mergesort(arr[:int(len(arr)//2)-1])
        rarr=self.mergesort(arr[int(len(arr)//2):])



        lidx=0
        ridx=0
        while len(larr)-1 != lidx and len(rarr)-1!=ridx:
            if larr[lidx]<rarr[ridx]:
                retar+=larr[lidx]
                lidx+=1
            else:
                retar+=rarr[ridx]
                ridx+=1

        while len(larr)-1 != lidx or len(rarr)-1!=ridx:
            if len(larr)-1 != lidx:
                retar+=larr[lidx]
                lidx+=1
            else:
                retar+=rarr[ridx]
                ridx+=1

        return retar




        


    

Solution.sortList()
