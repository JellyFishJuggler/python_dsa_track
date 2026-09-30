# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,head):
        curr = head
        prev = None
        
        while curr != None:

            dummy = curr.next
            curr.next = prev

            prev = curr
            curr = dummy
        return prev

    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:

        rev_head = self.reverse(head)
        curr = rev_head

        if n == 1:
            rev_head = rev_head.next
            return self.reverse(rev_head)

        if rev_head.next is None:
            return None

        count = 0
        while curr != None and curr.next != None:
            count += 1
            if count == n - 1:
                curr.next = curr.next.next
                break
            curr = curr.next
        
        return self.reverse(rev_head)