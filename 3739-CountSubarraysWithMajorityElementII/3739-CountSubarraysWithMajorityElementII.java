// Last updated: 6/27/2026, 1:17:53 AM
1class Solution {
2    public long countMajoritySubarrays(int[] nums, int target) {
3        int n = nums.length;
4        long res = 0;
5
6        for (int i = 0; i < n; i++) {
7            if (nums[i] == target) nums[i] = 1;
8            else nums[i] = -1;
9        }
10
11        int[] pref = new int[n];
12        pref[0] = nums[0];
13
14        for (int i = 1; i < n; i ++) {
15            pref[i] = pref[i - 1] + nums[i];
16        }
17
18        int shift = n;
19        int[] freq = new int[2 * n + 1];
20
21        freq[shift] = 1;
22
23
24        long valid = 0;
25        int lastSum = 0;
26
27        for (int i = 0; i < n; i++) {
28            if (pref[i] > lastSum) {
29                valid += freq[lastSum + shift];
30            } else {
31                valid -= freq[pref[i] + shift];
32            }
33
34            res += valid;
35            freq[pref[i] + shift]++;
36            lastSum = pref[i];
37        }
38
39        return res;
40
41    }
42}