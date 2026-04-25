// Last updated: 4/25/2026, 11:43:10 PM
1class Solution {
2    public int furthestDistanceFromOrigin(String moves) {
3        int n = moves.length();
4        int countL = 0;
5        int countR = 0;
6        int countUnderscore = 0;
7
8        for (int i = 0; i < n; i ++) {
9            char c = moves.charAt(i);
10            if (c == 'L') {
11                countL += 1;
12            } else if(c == 'R') {
13                countR += 1;
14            } else if (c == '_') {
15                countUnderscore += 1;
16            }
17        }
18        int positionAllL = (countL + countUnderscore) - countR;
19        int positionAllR = countL - (countR + countUnderscore);
20        return Math.max(Math.abs(positionAllL), Math.abs(positionAllR));
21    }
22}