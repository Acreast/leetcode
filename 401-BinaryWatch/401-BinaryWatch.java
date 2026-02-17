// Last updated: 2/18/2026, 12:43:13 AM
1class Solution {
2    public List<String> readBinaryWatch(int k) {
3        if (k == 0) {
4            return List.of("0:00");
5        }
6        int mask = ( 1 << 6) - 1;
7        int q = (1 << k) - 1;
8        int limit = q << (10 - k);
9        List<String> res = new ArrayList<>();
10
11        while(q <= limit) {
12            int min = q & mask;
13            int hour = q >> 6;
14            if (hour < 12 && min < 60) {
15                res.add(hour + ":" + (min < 10 ? "0" : "") + min);
16            }
17
18            int r = q & -q;
19            int n = q + r;
20            q = (((q ^ n) / r) >> 2) | n;
21        }
22        return res;
23    }
24}