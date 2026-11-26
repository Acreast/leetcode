# Last updated: 11/27/2026, 12:58:41 AM
1class Solution:
2    def canAliceWin(self, n: int) -> bool:
3        counter = 10
4        alice_turn = True
5        while n >= 0:
6            if n - counter == 0:
7                if alice_turn:
8                    return True
9                else:
10                    return False
11            elif n - counter < 0:
12                if alice_turn:
13                    return False
14                else:
15                    return True
16            alice_turn = not alice_turn
17            n -= counter
18            counter -= 1
19        return False
20        
21
22            
23
24            