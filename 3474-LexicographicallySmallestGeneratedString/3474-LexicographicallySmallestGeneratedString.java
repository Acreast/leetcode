// Last updated: 3/31/2026, 10:56:16 PM
1class Solution {
2    public String generateString(String str1, String str2) {
3        int n = str1.length();
4        int m = str2.length();
5
6        int L = n + m - 1;
7
8        char[] s1 = str1.toCharArray();
9        char[] s2 = str2.toCharArray();
10
11
12        char[] res = new char[L];
13        Arrays.fill(res,'?');
14
15        int[] z = calc_z(s2);
16
17        int last_s2 = -m;
18
19        for (int i = 0; i < n; i ++) {
20            if (s1[i] != 'T') continue;
21
22            int overlap = Math.max(last_s2 + m - i, 0);
23            if (overlap > 0 && z[m - overlap] < overlap) return "";
24
25            for (int j = overlap; j < m; j ++) {
26                res[i + j] = s2[j];
27            }
28            last_s2 = i;
29        }
30
31        int [] last_free = new int[L];
32        int curr = -1;
33        for (int i = 0; i < L; i ++) {
34            if (res[i] == '?') {
35                res[i] = 'a';
36                curr = i;
37            }
38            last_free[i] = curr;
39        }
40
41        char[] combined = new char[m + L];
42        System.arraycopy(s2, 0, combined, 0, m);
43        System.arraycopy(res, 0, combined, m, L);
44        int[] z_combined = calc_z(combined);
45
46        for (int i = 0; i < n; i ++) {
47            if (s1[i] != 'F') continue;
48
49            if (z_combined[m + i] >= m) {
50                int post_to_change = last_free[i + m - 1];
51                if (post_to_change < i) return "";
52
53                res[post_to_change] = 'b';
54
55                i = post_to_change;
56            }
57        }
58
59        return new String(res);
60    }
61
62    private int[] calc_z(char[] s2) {
63        int n = s2.length;
64        int[] z = new int[n];
65        int L = 0, R = 0;
66
67        for (int i = 1; i < n ; i ++) {
68            if  ( i <= R ) {
69                z[i] = Math.min(R - i + 1, z[i - L]);
70            }
71
72            while (i + z[i] < n && s2[z[i]] == s2[i + z[i]]) {
73                L = i;
74                R = i + z[i];
75                z[i] ++ ;
76            }
77        }
78
79        if (n > 0) z[0] = n;
80        return z;
81    }
82}