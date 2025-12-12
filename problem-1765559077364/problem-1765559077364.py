# Last updated: 12/13/2025, 1:04:37 AM
1class Solution:
2    def countMentions(self, n: int, events: List[List[str]]) -> List[int]:
3        mentions = [0]*n
4        back = [0]*n
5        events.sort(key=lambda e: (int(e[1]), e[0]=="MESSAGE"))
6
7        for typ, t, data in events:
8            t = int(t)
9            if typ == "OFFLINE":
10                back[int(data)] = t + 60
11                continue
12
13            for tok in data.split():
14                if tok == "ALL":
15                    for u in range(n):
16                        mentions[u] += 1
17                elif tok == "HERE":
18                    for u in range(n):
19                        if t >= back[u]:
20                            mentions[u] += 1
21                else:  
22                    mentions[int(tok[2:])] += 1
23
24        return mentions
25