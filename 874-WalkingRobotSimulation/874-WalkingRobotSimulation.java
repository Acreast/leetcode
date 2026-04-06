// Last updated: 4/6/2026, 11:23:09 PM
1class Solution {
2    public int robotSim(int[] commands, int[][] obstacles) {
3        int x = 0, y = 0, d = 0;
4        int[][] direction = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
5        int maxDistance = 0;
6
7        Set<String> obstacleSet = new HashSet<>();
8        for (int[] obstacle : obstacles) {
9            obstacleSet.add(obstacle[0] + "," + obstacle[1]);
10        }
11
12        for (int cmd : commands) {
13            if (cmd == -1) {
14                d = (d + 1) % 4;
15            } else if (cmd == -2) {
16                d = (d + 3) % 4;  // equivalent to (d - 1) % 4 in Python
17            } else {
18                for (int step = 0; step < cmd; step++) {
19                    int nx = x + direction[d][0];
20                    int ny = y + direction[d][1];
21                    if (obstacleSet.contains(nx + "," + ny)) {
22                        break;
23                    }
24                    x = nx;
25                    y = ny;
26                    maxDistance = Math.max(maxDistance, x * x + y * y);
27                }
28            }
29        }
30        return maxDistance;
31
32    }
33}