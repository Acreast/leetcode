# Last updated: 11/28/2025, 8:18:54 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
8        dummy = ListNode()
9        tail = dummy
10        while list1 and list2:
11            if list1.val < list2.val:
12                tail.next = list1
13                list1 = list1.next
14            else:
15                tail.next = list2
16                list2 = list2.next
17            tail = tail.next
18            
19        if list1:
20            tail.next = list1
21        elif list2:
22            tail.next = list2
23
24        return dummy.next
25
26