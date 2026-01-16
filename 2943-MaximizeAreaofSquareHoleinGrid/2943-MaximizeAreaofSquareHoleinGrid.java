// Last updated: 1/17/2026, 12:04:37 AM
1class Solution {
2    public int maximizeSquareArea(int m, int n, int[] hFences, int[] vFences) {
3        List<Integer> hList = new ArrayList<>();
4        for (int h : hFences) hList.add(h);
5        hList.add(1);
6        hList.add(m);
7
8        List<Integer> vList = new ArrayList<>();
9        for (int v : vFences) vList.add(v);
10        vList.add(1);
11        vList.add(n);
12
13        Set<Integer> gap_set = new HashSet<>();
14        long res = 0;
15
16        for (int i = 0; i < hList.size(); i++) {
17            for (int j = i + 1; j < hList.size(); j++) {
18                gap_set.add(Math.abs(hList.get(j) - hList.get(i)));
19            }
20        }
21
22        for (int i = 0; i < vList.size(); i++) {
23            for (int j = i + 1; j < vList.size(); j++) {
24                int gap = Math.abs(vList.get(j) - vList.get(i));
25                if (gap_set.contains(gap)) {
26                    res = Math.max(res, gap);
27                }
28            }
29        }
30
31
32        if (res == 0) {
33            return -1;
34        }
35        long MOD = 1_000_000_007;
36        return (int) ((res * res) % MOD);
37    }
38}