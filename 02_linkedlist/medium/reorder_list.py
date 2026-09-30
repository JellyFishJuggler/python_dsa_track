# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        curr = head
        # n = 0
        idx = []
        while curr != None:
            idx.append(curr)
            # idx[n] = n
            # n += 1
            curr = curr.next
        curr = head

        d = ListNode()
        tail = d

        i = 0
        j = len(idx) - 1
        while i <= j:
            if i == j:
                tail.next = idx[i]
                tail = tail.next
            else:
                tail.next = idx[i]
                tail = tail.next
                tail.next = idx[j]
                tail = tail.next
                # d.append(idx[i])
                # d.append(idx[j])
            i += 1
            j -= 1
        tail.next = None
        