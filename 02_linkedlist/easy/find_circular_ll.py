# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # s = set()
        # curr = head

        # while curr != None:
        #     if curr in s:
        #         return True
            
        #     s.add(curr)
        #     curr = curr.next

        curr = head
        fast = curr
        slow = curr

        while curr != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
            if fast == None:
                return False
            if fast == slow:
                return True
        return False