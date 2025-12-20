# Last updated: 12/20/2025, 3:47:21 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
8        
9        res = ListNode()
10        cur = res
11        carry = 0
12
13        while l1 or l2 or carry:
14            l1_val = l1.val if l1 else 0
15            l2_val = l2.val if l2 else 0
16
17            cur_val = l1_val + l2_val + carry
18            carry = cur_val // 10
19            cur_val = cur_val % 10
20
21            cur.next = ListNode(cur_val)
22            cur = cur.next
23
24            l1 = l1.next if l1 else None
25            l2 = l2.next if l2 else None
26            
27        return res.next
28            
29
30
31
32        