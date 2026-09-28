# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def split(self, head: Listnode | None) -> ListNode | None:

        left = head
        right = head
        curr = head
        n = 0
        while curr != None:
            n += 1
            curr = curr.next
        curr = head
        mid = n // 2
        
        for i in range(mid - 1):
            curr = curr.next
        right = curr.next
        curr.next = None
        return left, right

    def merge(self,left, right):

        dummy = ListNode()
        curr = dummy
        curr1 = left
        curr2 = right

        while curr1 != None and curr2 != None:
            
            # if curr2 == None:
            #     curr.next = curr1
            # if curr1 == None:
            #     curr.next = curr2

            if curr1.val < curr2.val:
                curr.next = curr1
                curr1 = curr1.next
            else:
                curr.next = curr2
                curr2 = curr2.next
            curr = curr.next
        if curr1 != None:
            curr.next = curr1
        else:
            curr.next = curr2
        return dummy.next
    def sortList(self, head: ListNode | None) -> ListNode | None:
        
        curr = head
        # # prev = head
        if curr == None or curr.next == None:
            return head

        n = 0
        while curr != None:
            n += 1
            curr = curr.next
        # i = 0
        # while i < n:
        #     curr = head
        #     while curr != None and curr.next != None:
        #         val = curr.val
        #         next_val = curr.next.val
        #         if next_val < val:
        #             curr.val, curr.next.val = curr.next.val,curr.val
        #         curr = curr.next
        #         # prev = prev.next
        #     # curr = curr.next
        #     i += 1
        l,r = self.split(head)
        l = self.sortList(l)
        r = self.sortList(r)

        return self.merge(l,r)
    