# Last updated: 7/14/2025, 10:53:00 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        res = 0
        string = ""
        while head:
            string = string + str(head.val)
            head = head.next
        
        for i in range(len(string)):
            res += (2 ** (len(string) - 1 - i)) * int(string[i])

        return res