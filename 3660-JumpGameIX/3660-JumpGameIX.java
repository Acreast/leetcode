// Last updated: 5/7/2026, 10:39:47 PM
1class Solution {
2    public int[] maxValue(int[] nums) {
3        int n = nums.length;
4        int [] suffixMin = new int[n + 1];
5        suffixMin[n] = Integer.MAX_VALUE;
6        for (int i = n - 1; i >= 0; i --) {
7            suffixMin[i] = Math.min(nums[i], suffixMin[i + 1]);
8        }
9
10        int[] ans = new int[n];
11        int l = 0;
12
13        while (l < n) {
14            int r = l;
15            int maxVal = nums[l];
16
17            while (r + 1 < n && maxVal > suffixMin[r + 1]) {
18                r ++;
19                maxVal = Math.max(maxVal, nums[r]);
20            }
21
22            for (int i = l; i <= r; i ++) {
23                ans[i] = maxVal;
24            }
25
26            l = r + 1;
27        }        
28
29        return ans;
30    }
31}