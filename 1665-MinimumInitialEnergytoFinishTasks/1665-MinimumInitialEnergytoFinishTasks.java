// Last updated: 5/12/2026, 11:08:03 PM
1class Solution {
2    public int minimumEffort(int[][] tasks) {
3        Arrays.sort(tasks, (a,b) -> b[1] - b[0] - (a[1] - a[0]));
4
5        int start = tasks[0][1];
6        int bal = tasks[0][1] - tasks[0][0];
7        int own = 0;
8
9        for( int i = 1; i < tasks.length; i ++) {
10            int cost = tasks[i][0];
11            int thresh = tasks[i][1];
12
13            if (bal < thresh) {
14                own += thresh - bal;
15                bal = thresh;
16            }
17
18            bal -= cost;
19        }
20
21
22        return start + own;
23    }
24}