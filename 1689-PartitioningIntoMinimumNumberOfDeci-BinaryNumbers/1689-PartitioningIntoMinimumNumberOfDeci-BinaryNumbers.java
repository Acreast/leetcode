// Last updated: 3/1/2026, 8:33:53 PM
1class Solution {
2    public int minPartitions(String n) {
3        for (char ch = '9'; ch >= '0'; ch --) {
4            if (n.indexOf(ch) != - 1) {
5                return ch - '0';
6            }
7        }
8        return -1;
9    }
10}