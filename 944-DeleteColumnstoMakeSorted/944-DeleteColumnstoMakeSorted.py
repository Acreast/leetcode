# Last updated: 12/21/2025, 5:08:19 PM
1class Solution:
2    def minDeletionSize(self, strs: List[str]) -> int:
3        n = len(strs)
4        m = len(strs[0])
5        res = 0
6
7        duplicate = [True] * (n - 1)
8
9        for col in range(m):
10            delete = False
11
12            for i in range(n - 1):
13                if duplicate[i] and strs[i][col] > strs[i + 1][col]:
14                    delete = True
15                    break
16
17            if delete:
18                res += 1
19                continue
20
21            for i in range(n - 1):
22                if duplicate[i] and strs[i][col] < strs[i + 1][col]:
23                    duplicate[i] = False
24
25            # Optimization: if no duplicates remain, we're done
26            if not any(duplicate):
27                break
28
29        return res