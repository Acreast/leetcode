// Last updated: 4/14/2026, 11:53:42 PM
1class Solution {
2    public long minimumTotalDistance(List<Integer> robot, int[][] factory) {
3        Collections.sort(robot);
4        Arrays.sort(factory, (a, b) -> a[0] - b[0]);
5
6        int r = robot.size();
7        int f = factory.length;
8
9        long[][] dp = new long[r+1][f + 1];
10
11        for (int i = 0; i<= r; i ++) {
12            Arrays.fill(dp[i], Long.MAX_VALUE / 2);
13        }
14
15        for (int j = 0; j <= f; j ++) {
16            dp[0][j] = 0;
17        }
18
19        for (int j = 1; j <= f; j ++) {
20            int pos = factory[j -1][0];
21            int limit = factory[j - 1][1];
22
23            for (int i = 0; i <= r; i ++) {
24                dp[i][j] = dp[i][j - 1];
25
26                long dist = 0;
27
28                for (int k = 1; k <= limit && i - k >=0; k ++) {
29                    dist += Math.abs(robot.get(i - k) - pos);
30                    dp[i][j] = Math.min(dp[i][j] , dp[i - k][ j - 1] + dist);
31                }
32            }
33
34        }
35        return dp[r][f];
36
37    }
38}