# Last updated: 8/29/2026, 1:11:08 AM
1class Solution:
2    def lexPalindromicPermutation(self, s: str, target: str) -> str:
3        freq = Counter(s)
4        
5        def check() -> bool:
6            return all(v >= 0 for v in freq.values())
7
8        center = ''
9        for x, v in freq.items():
10            if v % 2 == 0: continue
11            if center: return ""
12            center = x
13            freq[x] -= 1
14
15        sz = len(s)
16        half = sz // 2
17        for i, w in enumerate(target[:half]):
18            freq[w] -= 2
19
20        if check():
21            head = target[:half]
22            tail = center + head[::-1]
23            if tail > target[half:]:
24                return head + tail
25
26        for i in range(half - 1, -1, -1):
27            w = target[i]
28            freq[w] += 2
29            if not check(): continue
30
31            for j in range(ord(w) - ord('a') + 1, 26):
32                x = ascii_lowercase[j]
33                if freq[x] == 0: continue
34
35                freq[x] -= 2
36                result = list(target[:i + 1])
37                result[i] = x
38
39                for x in ascii_lowercase:
40                    result.extend(x * (freq[x] // 2))
41
42                tail = result[::-1]
43                result.append(center)
44                result += tail
45
46                return ''.join(result)
47
48        return ""