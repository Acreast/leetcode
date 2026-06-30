// Last updated: 7/1/2026, 12:08:19 AM
1class Solution {
2    public int numberOfSubstrings(String s) {
3        int[] freq = new int[3];
4        int res = 0;
5        int l = 0;
6        for (int r = 0; r < s.length(); r ++) {
7            freq[s.charAt(r) - 'a']++;
8
9            while (
10                freq[0] > 0 &&
11                freq[1] > 0 &&
12                freq[2] > 0 
13                ) {
14                    res += s.length() - r;
15                    freq[s.charAt(l) - 'a']--;
16                    l++;
17                }
18        }
19
20        return res;
21
22    }
23}