# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:

        m = 0
        count = 0
        curr = head

        while curr != None:
            count += 1
            curr = curr.next
        
        m = count // 2

        for i in range(m):
            head = head.next
        return head