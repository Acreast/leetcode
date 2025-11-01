# Last updated: 11/2/2025, 12:10:10 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        
        nums = set(nums)
        cur = head
        placeholder = ListNode(0, head)
        prev = placeholder
        while cur:
            if cur.val in nums:
                prev.next = cur.next
            else:
                prev = prev.next
            cur = cur.next
        
        return placeholder.next
