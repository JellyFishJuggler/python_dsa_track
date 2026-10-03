# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    # def traversal(self,head,direction):

    #     curr = head
    #     while curr != None and curr.val != direction:
    #         curr = curr.next
    #     return curr            

    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:

        prev = head
        temp = ListNode(0)
        temp.next = head
        # l_prev = head.next
        # l = self.traversal(head,left)
        # r = self.traversal(head,right)

        prev = temp

        for i in range(left - 1):
            prev = prev.next
        curr = prev.next

        for i in range(right - left):
            # l_prev.next = prev
            # l.next = curr
            nextNode = curr.next
            curr.next = nextNode.next
            nextNode.next = prev.next
            prev.next = nextNode
            # curr = nextNode
        # head = prev
        # l.next = prev
        return temp.next