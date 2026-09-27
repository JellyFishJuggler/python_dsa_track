    # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        A = headA
        B = headB
        
        if A == B:
            return A
        
        lenA = 0
        lenB = 0

        while A != None:
            lenA += 1
            A = A.next
        
        while B != None:
            lenB += 1
            B = B.next
        
        A = headA
        B = headB

        value = headA
        diff = abs(lenA - lenB)

        if lenA > lenB:
            for i in range(diff):
                A = A.next
        if lenB > lenA:
            for i in range(diff):
                B = B.next

        while A != None and B != None:
            if A == B:
                return A
            A = A.next
            B = B.next
        return None