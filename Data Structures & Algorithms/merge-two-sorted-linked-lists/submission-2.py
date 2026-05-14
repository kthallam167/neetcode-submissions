# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        elif list2 == None:
            return list1
        dummyhead = None
        if list1.val>list2.val:
            dummyhead = list2
            list2 = list2.next
        else:
            dummyhead = list1
            list1 = list1.next
        original = dummyhead
        while list1!=None or list2!=None:
            if list1==None:
                dummyhead.next = list2
                return original
            elif list2==None:
                dummyhead.next = list1
                print("2")
                return original
            elif list1.val<list2.val:
                dummyhead.next = list1
                list1 = list1.next
                dummyhead = dummyhead.next
            else:
                dummyhead.next = list2
                list2 = list2.next
                dummyhead = dummyhead.next

        print("3")
        return original
