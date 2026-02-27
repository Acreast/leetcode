// Last updated: 2/28/2026, 12:07:53 AM
1class Solution {
2    public int minOperations(String s, int k) {
3        int zero = 0;
4        int len = s.length();
5
6        for (int i = 0; i < len; i++)
7            zero += ~s.charAt(i) & 1;
8
9        if (zero == 0)
10            return 0;
11
12        if (len == k)
13            return (zero == len ? 1 : -1);
14
15        int base = len - k;
16
17        int odd = Math.max(
18            (zero + k - 1) / k,
19            (len - zero + base - 1) / base
20        );
21
22        odd += ~odd & 1;
23
24        int even = Math.max(
25            (zero + k - 1) / k,
26            (zero + base - 1) / base
27        );
28
29        even += even & 1;
30
31        int res = Integer.MAX_VALUE;
32
33        if ((k & 1) == (zero & 1))
34            res = Math.min(res, odd);
35
36        if ((~zero & 1) == 1)
37            res = Math.min(res, even);
38
39        return res == Integer.MAX_VALUE ? -1 : res;
40    }
41}