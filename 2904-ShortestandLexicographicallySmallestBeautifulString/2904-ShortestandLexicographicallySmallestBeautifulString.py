# Last updated: 8/28/2026, 1:15:53 AM
1class Solution:
2    def lexGreaterPermutation(self, s: str, target: str) -> str:
3        cnt = [0] * 26
4
5        for ch in s:
6            cnt[ord(ch) - ord('a')] += 1
7
8        for ch in target:
9            cnt[ord(ch) - ord('a')] -= 1
10        
11        for i in range(len(target) - 1, - 1, -1):
12            cur = ord(target[i]) - ord('a')
13            cnt[cur] += 1
14
15            if any (x < 0 for x in cnt):
16                continue
17            
18            nxt = -1
19            for c in range(cur + 1, 26):
20                if cnt[c]:
21                    nxt = c
22                    break
23                
24            if nxt == -1:
25                continue
26            
27            cnt[nxt] -= 1
28
29            res = list(target[:i])
30            res.append(chr(nxt+ord('a')))
31
32            for c in range(26):
33                res.extend(chr(c + ord('a')) * cnt[c])
34            
35            return ''.join(res)
36        
37        return ""
38
39
40