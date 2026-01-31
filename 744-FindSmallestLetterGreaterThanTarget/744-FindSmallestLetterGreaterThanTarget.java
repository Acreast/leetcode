// Last updated: 1/31/2026, 11:39:12 PM
1class Solution {
2    public char nextGreatestLetter(char[] letters, char target) {
3        char res = letters[0];
4        boolean threshold_reached = false;
5        for(char c : letters) {
6            if (!threshold_reached) {
7                if (c > target) {
8                    res = c;
9                    threshold_reached = !threshold_reached;
10                }
11            } else {
12                if(c > target && c < res) res = c;
13            }
14        }
15
16        return res;
17    }
18}