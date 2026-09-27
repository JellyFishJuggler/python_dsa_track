# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:

        if list1 == None:
            return list2
        if list2 == None:
            return list1
        
        if list1.val > list2.val:
            list1,list2 = list2,list1

        curr1 = list1
        curr2 = list2

        while curr1 != None and curr2 != None:

            next1 = curr1.next
            next2 = curr2.next

            if curr1.val <= curr2.val and (curr1.next == None or curr1.next.val >= curr2.val):
                curr2.next = curr1.next
                curr1.next = curr2
                curr2 = next2
            else:
                curr1 = curr1.next

        return list1