# Last updated: 12/19/2025, 10:13:57 PM
1"""
2# Definition for a Node.
3class Node:
4    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
5        self.val = int(x)
6        self.next = next
7        self.random = random
8"""
9
10class Solution:
11    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
12        
13        replica = {None:None}
14        cur = head
15        while cur:
16            new_node = Node(cur.val)
17            replica[cur] = new_node
18            cur = cur.next
19        
20        cur = head
21        while cur:
22            replicated_node = replica[cur]
23            replicated_node.next = replica[cur.next]
24            replicated_node.random = replica[cur.random]
25            cur = cur.next
26        
27        return replica[head]
28        