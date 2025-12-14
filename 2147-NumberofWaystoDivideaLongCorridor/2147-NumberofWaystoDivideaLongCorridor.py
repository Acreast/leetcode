# Last updated: 12/14/2025, 11:43:22 PM
1class Solution:
2    def numberOfWays(self, corridor: str) -> int:
3        MOD = 10 ** 9 + 7
4        res = 1
5        temp = 0
6        count = 0
7
8        for i in range(len(corridor)):
9            if count != 2:
10                if corridor[i] == 'S':
11                    count += 1
12            else:
13                if corridor[i] == 'S':
14                    temp += 1
15                    res *= temp
16                    res %= MOD
17                    count = 1
18                    temp = 0
19                else:
20                    temp += 1
21
22        if count != 2:
23            return 0
24        else:
25            return res
26
27