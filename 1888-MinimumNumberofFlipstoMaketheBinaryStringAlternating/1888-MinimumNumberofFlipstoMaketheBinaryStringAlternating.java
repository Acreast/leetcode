// Last updated: 3/8/2026, 1:51:15 AM
1class Solution {
2    public int minFlips(String s) {
3        int n = s.length();                     // length of original string
4        String t = s + s;                        // doubled string – contains every rotation
5        int count0 = 0, count1 = 0;               // mismatches for pattern0 (starting with 0) and pattern1
6
7        // ---------- first window (shift = 0) ----------
8        for (int j = 0; j < n; j++) {
9            char expected = t.charAt(j);          // character at position j in the first window
10
11            // compare with pattern0 (even positions '0', odd positions '1')
12            if (expected != (j % 2 == 0 ? '0' : '1')) count0++;
13            // compare with pattern1 (even positions '1', odd positions '0')
14            if (expected != (j % 2 == 0 ? '1' : '0')) count1++;
15        }
16
17        int min_flips = Math.min(count0, count1); // best for the initial window
18
19        // ---------- slide the window n-1 more times ----------
20        for (int i = 1; i < n; i++) {
21            // character that leaves the window (was at the beginning of previous window)
22            char old_char = t.charAt(i - 1);
23            // character that enters the window (becomes the last character of new window)
24            char new_char = t.charAt(i + n - 1);
25
26            // contribution of old_char in the *previous* window:
27            // it was at position 0, so for pattern0 it contributed if it was not '0'
28            int contrib0 = (old_char != '0') ? 1 : 0;
29            // for pattern1 it contributed if it was not '1'
30            int contrib1 = (old_char != '1') ? 1 : 0;
31
32            // parity of the last position (n-1) in the new window – needed for new_char
33            boolean last_pos_char = ((n - 1) % 2 == 0);
34
35            // contribution of new_char in the *new* window at last position
36            int new_contrib0 = (new_char != (last_pos_char ? '0' : '1')) ? 1 : 0;
37            int new_contrib1 = (new_char != (last_pos_char ? '1' : '0')) ? 1 : 0;
38
39            // ---- update the counters using the inversion trick ----
40            // (n-1) - (count0 - contrib0)  → mismatches among the n-1 middle characters after their parities flip
41            // then add the contribution of the new character
42            count0 = (n - 1) - (count0 - contrib0) + new_contrib0;
43            count1 = (n - 1) - (count1 - contrib1) + new_contrib1;
44
45            // keep the global minimum
46            min_flips = Math.min(min_flips, Math.min(count0, count1));
47        }
48
49        return min_flips;
50    }
51}