// Last updated: 3/29/2026, 7:19:14 PM
1class Solution {
2    public boolean canBeEqual(String s1, String s2) {
3        
4        char[] even1 = {s1.charAt(0), s1.charAt(2)};
5        char[] even2 = {s2.charAt(0), s2.charAt(2)};
6        char[] odd1 = {s1.charAt(1), s1.charAt(3)};
7        char[] odd2 = {s2.charAt(1), s2.charAt(3)};
8
9        Arrays.sort(even1);
10        Arrays.sort(even2);
11        Arrays.sort(odd1);
12        Arrays.sort(odd2);
13
14        return Arrays.equals(even1,even2) && Arrays.equals(odd1,odd2);
15        
16    }
17}