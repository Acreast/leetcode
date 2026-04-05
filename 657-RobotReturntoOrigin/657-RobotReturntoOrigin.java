// Last updated: 4/5/2026, 5:01:08 PM
1class Solution {
2    public boolean judgeCircle(String moves) {
3        int x = 0;
4        int y = 0;
5        for (char c:moves.toCharArray()) {
6            if (c == 'U') {
7                y += 1;
8            } else if (c == 'D') {
9                y -= 1;
10            } else if (c == 'L') {
11                x -= 1;
12            } else if (c == 'R') {
13                x += 1;
14            }
15        }
16
17        return (x == 0 && y == 0);
18    }
19}