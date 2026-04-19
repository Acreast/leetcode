// Last updated: 4/20/2026, 12:41:25 AM
1class Solution {
2    public int maxDistance(int[] nums1, int[] nums2) {
3        int maxDist = Integer.MIN_VALUE, n = nums1.length, m = nums2.length;
4
5        int i = 0, j = 0;
6        while (i < n && j < m) {
7            if (i <= j && nums1[i] <= nums2[j]) {
8                int dist = j - i;
9                maxDist = Math.max(maxDist, dist);
10                j++;
11            } else {
12                if (i <= j && nums1[i] > nums2[j]) {
13                    i++;
14                } else if (i > j) {
15                    j++;
16                }
17            }
18        }
19
20        return maxDist == Integer.MIN_VALUE ? 0 : maxDist;
21    }
22}