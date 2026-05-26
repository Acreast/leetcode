// Last updated: 5/27/2026, 1:21:38 AM
1class Solution {
2    public int numberOfSpecialChars(String word) {
3        int lower = 0;
4        int upper = 0;
5
6        for(char ch : word.toCharArray()) {
7            if(Character.isLowerCase(ch)) {
8                lower |= (1 << (ch - 'a'));
9            }
10            else {
11                upper |= (1 << (ch - 'A'));
12            }
13        }
14
15        int common = lower & upper;
16
17        // counting number of set bits
18        return Integer.bitCount(common);
19    }
20}