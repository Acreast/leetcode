// Last updated: 2/1/2026, 11:33:02 PM
1class Solution {
2    public char nextGreatestLetter(char[] letters, char target) {
3        for(char c : letters) {
4            if (c > target) {
5                return c;
6            }
7        }
8        return letters[0];
9    }
10}