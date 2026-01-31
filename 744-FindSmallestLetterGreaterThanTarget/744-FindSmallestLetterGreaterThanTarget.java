// Last updated: 1/31/2026, 11:23:07 PM
1class Solution {
2    public char nextGreatestLetter(char[] letters, char target) {
3        int smallest_ord = Integer.MAX_VALUE;
4        char res = letters[0];
5        for(char c : letters) {
6            int ord = c - target;
7            if (ord < 1) {
8                continue;
9            }
10            if (ord < smallest_ord) {
11                res = c;
12                smallest_ord = ord;
13            }
14        }
15
16        return res;
17    }
18}