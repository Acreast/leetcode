# Last updated: 11/29/2025, 7:18:41 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reorderList(self, head: Optional[ListNode]) -> None:
8        slow = head
9        fast = slow.next
10
11        while fast and fast.next:
12            slow = slow.next
13            fast = fast.next.next
14        
15        second_half = slow.next
16        # Detach the first half
17        slow.next = None
18        prev = None
19
20        # Flip second half
21        while second_half:
22            temp = second_half.next
23            second_half.next = prev
24            prev = second_half
25            second_half = temp
26        
27        first_half, second_half = head, prev
28        while second_half:
29            node1, node2 = first_half.next, second_half.next
30            first_half.next = second_half
31            second_half.next = node1
32            first_half = node1
33            second_half = node2
34
35
36        