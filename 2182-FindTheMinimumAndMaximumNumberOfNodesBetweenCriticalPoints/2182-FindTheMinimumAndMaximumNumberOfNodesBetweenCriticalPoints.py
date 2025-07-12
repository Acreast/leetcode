# Last updated: 7/12/2025, 11:47:50 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        min_dist, max_dist = float("inf"), -1

        index = 1
        def is_critical(prev,cur,next):
            return (
                (prev.val < cur.val > next.val) or
                (prev.val > cur.val < next.val)
            )
        
        prev = head
        cur = head.next
        next = cur.next
        index = 1

        first_crit_index = 0
        prev_crit_index = 0

        while next:
            if is_critical(prev,cur,next):
                if first_crit_index:
                    max_dist = index - first_crit_index
                    min_dist = min (
                        min_dist,
                        index - prev_crit_index
                    )
                else:
                    first_crit_index = index
                prev_crit_index = index

            prev, cur, next = cur, next, next.next
            index += 1
        
        if min_dist == float("inf"):
            min_dist = -1

        return [min_dist,max_dist] 
