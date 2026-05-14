// Last updated: 5/14/2026, 11:00:51 PM
1class Solution {
2    public boolean isGood(int[] nums) {
3        int n = nums.length;
4        int max = n - 1;
5        int[] freq = new int[n];
6        for (int num: nums){
7
8            if (num < 1 || num > max) {
9                return false;
10            }
11            freq[num] ++;
12        }
13
14        for (int i = 1; i < max; i ++) {
15            if (freq[i] != 1 ) {
16                return false;
17            }
18        }
19
20        return freq[max] == 2;
21    }
22}