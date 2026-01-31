// Last updated: 1/31/2026, 11:40:37 PM
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