// Last updated: 7/25/2026, 1:41:14 AM
1class Solution {
2    public int uniqueXorTriplets(int[] nums) {
3        int n = nums.length;
4
5        int[] pairXor = new int[2048];
6        int[] tripleXor = new int[2048];
7
8        // Compute all possible pair XORs
9        for (int i = 0; i < n; i++) {
10            for (int j = i; j < n; j++) {
11                pairXor[nums[i] ^ nums[j]] = 1;
12            }
13        }
14
15        // Generate triplet XORs
16        for (int i = 0; i < n; i++) {
17            for (int j = 0; j < 2048; j++) {
18                if (pairXor[j] == 1) {
19                    tripleXor[j ^ nums[i]] = 1;
20                }
21            }
22        }
23
24        // Count distinct XOR values
25        int cnt = 0;
26        for (int value : tripleXor) {
27            if (value == 1) {
28                cnt++;
29            }
30        }
31
32        return cnt;
33    }
34}