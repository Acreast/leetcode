# Last updated: 7/23/2026, 1:39:33 AM
1class Solution:
2    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
3        ones = s.count('1')
4
5        # maximal zero-blocks (inclusive ends), unzipped into starts / ends
6        zs, ze = zip(*((mo.start(), mo.end() - 1) for mo in re.finditer('0+', s))) if '0' in s else ((), ())
7        nblocks = len(zs)
8
9        # valley j: full value = sum of the two adjacent run lengths
10        V = list(map(sum, pairwise(b - a + 1 for a, b in zip(zs, ze))))
11
12
13        nv = len(V)
14        sparse = [V]
15        half = 1
16        while half * 2 <= nv:
17            prev = sparse[-1]
18            sparse.append(list(map(max, prev, prev[half:])))
19            half *= 2
20
21        def rmq(lo, hi):                              # inclusive max over V[lo..hi]
22            t = (hi - lo + 1).bit_length() - 1
23            return max(sparse[t][lo], sparse[t][hi - (1 << t) + 1])
24
25        def clip(j, l, r):                            # valley j's gain, clipped to [l, r]
26            return V[j] - max(0, l - zs[j]) - max(0, ze[j + 1] - r)
27
28        def gain(l, r):
29            if nblocks < 2:
30                return 0
31            ja = bisect_left(ze, l)                   # first usable valley: left run ends >= l
32            jb = bisect_right(zs, r) - 2              # last  usable valley: right run starts <= r
33            if ja > jb:
34                return 0
35            return max(clip(ja, l, r), clip(jb, l, r), rmq(ja + 1, jb - 1) if jb - ja >= 2 else 0)
36
37        return [ones + gain(l, r) for l, r in queries]
38
39        
40
41        return res