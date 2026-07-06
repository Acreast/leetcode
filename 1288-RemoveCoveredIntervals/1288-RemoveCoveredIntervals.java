// Last updated: 7/7/2026, 12:34:46 AM
1class Solution {
2    public int removeCoveredIntervals(int[][] intervals) {
3        int res = 0;
4        int left = -1;
5        int right = -1;
6        Arrays.sort(intervals, (a,b) -> Integer.compare(a[0],b[0]));
7        for(int[] arr : intervals) {
8            
9            if (arr[0] > left && arr[1] > right) {
10                left = arr[0];
11                ++res;
12            }
13            right = Math.max(right, arr[1]);
14        }
15        return res;
16    }
17}