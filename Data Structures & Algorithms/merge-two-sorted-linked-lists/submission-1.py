# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        myhead = None
        otherhead = None
        if list1 == None:
            return list2
        elif list2 == None:
            return list1
        if list1.val<list2.val:
            myhead = list1
            otherhead = list2
        else:
            myhead = list2
            otherhead = list1
        org = myhead
        while otherhead!=None and myhead!=None:
            if myhead.val<=otherhead.val and (myhead.next==None or otherhead.val<=myhead.next.val):
                tmp = otherhead
                otherhead = otherhead.next
                oldnext = myhead.next
                myhead.next = tmp
                tmp.next = oldnext
                myhead = myhead.next
            else:
                myhead = myhead.next

        return org
