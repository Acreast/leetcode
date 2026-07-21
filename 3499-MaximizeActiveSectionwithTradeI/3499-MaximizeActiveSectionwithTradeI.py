# Last updated: 7/22/2026, 1:12:37 AM
1class Solution:
2    def maxActiveSectionsAfterTrade(self, s: str) -> int:
3        ones = s.count('1')
4
5        s = '1' + s + '1'
6
7        n = len(s)
8        i = 0
9
10        res = ones
11
12        while i < n and s[i] == '1':
13            i += 1
14        
15        c10 = 0
16        while i < n and s[i] == '0':
17            c10 += 1
18            i += 1
19        
20        while i < n:
21            c11 = 0
22            while i < n and s[i] == '1':
23                c11 += 1
24                i += 1
25            
26            if c11 == 0:
27                break
28            
29            c20 = 0
30            while i < n and s[i] == '0':
31                c20 += 1
32                i += 1
33            
34            if c20 == 0:
35                break
36            
37            res = max(res, ones + c10 + c20)
38            c10 = c20
39        return res