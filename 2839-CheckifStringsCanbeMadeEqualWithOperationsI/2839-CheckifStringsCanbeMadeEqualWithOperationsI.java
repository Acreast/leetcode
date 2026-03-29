// Last updated: 3/29/2026, 7:38:39 PM
1class Solution {
2    public boolean canBeEqual(String s1, String s2) {
3        
4        int[] even = new int[26];
5        int[] odd = new int[26];
6
7        for (int i = 0; i < s1.length(); i++) {
8            if (i % 2 == 0) {
9                even[s1.charAt(i) - 'a']++;
10                even[s2.charAt(i) - 'a']--;
11            } else {
12                odd[s1.charAt(i) - 'a']++;
13                odd[s2.charAt(i) - 'a']--;
14            }
15        }
16
17        for (int i = 0; i < 26; i++) {
18            if (even[i] != 0 || odd[i] != 0) {
19                return false;
20            }
21        }
22
23        return true;
24        
25    }
26}