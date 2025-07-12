# Last updated: 7/12/2025, 11:44:17 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def common_divisors(curr_elem, next_elem):
            larger_elem = max(curr_elem, next_elem)
            smaller_elem = min(curr_elem, next_elem)
            while True:
                if larger_elem % smaller_elem == 0:
                    return smaller_elem
                larger_elem, smaller_elem = smaller_elem, larger_elem % smaller_elem
            return 0
        cur = head
        while cur.next != None:
            cur.next = ListNode(common_divisors(cur.val, cur.next.val), cur.next)
            cur = cur.next.next
                
        return head
            