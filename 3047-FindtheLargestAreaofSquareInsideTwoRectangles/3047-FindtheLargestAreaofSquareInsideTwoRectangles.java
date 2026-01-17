// Last updated: 1/17/2026, 11:33:57 PM
1class Solution {
2    public long largestSquareArea(int[][] bottomLeft, int[][] topRight) {
3        int s = 0;
4        int n = bottomLeft.length;
5
6        for (int i = 0; i < n; i ++) {
7            for (int j = i + 1; j < n; j ++) {
8                int minX = Math.max(bottomLeft[i][0], bottomLeft[j][0]);
9                int maxX = Math.min(topRight[i][0], topRight[j][0]);
10                int minY = Math.max(bottomLeft[i][1], bottomLeft[j][1]);
11                int maxY = Math.min(topRight[i][1], topRight[j][1]);
12
13                if (minX < maxX && minY < maxY) {
14                    int len = Math.min(maxX - minX, maxY - minY);
15                    s = Math.max(s, len);
16                }
17            }
18        }
19        return (long) s * s;
20    }
21}