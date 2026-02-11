// Last updated: 2/12/2026, 12:15:37 AM
1class Solution {
2    public int longestBalanced(int[] nums) {
3        int n = nums.length;
4
5        int[] balance = new int[n]; // first-occurrence markers for current l
6        HashMap<Integer, Integer> first = new HashMap<>(); // val -> first occurrence idx
7
8        int result = 0;
9        for (int l = n - 1; l >= 0; l--) {
10            int x = nums[l];
11
12            // If x already had a first occurrence to the right, remove that old marker.
13            Integer oldpos = first.get(x);
14            if (oldpos != null)
15                balance[oldpos] = 0;
16
17            // Now x becomes first occurrence at l.
18            first.put(x, l);
19            balance[l] = ((x & 1) == 0) ? 1 : -1;
20
21            // Find rightmost r >= l such that sum(balance[l..r]) == 0
22            int s = 0;
23            for (int r = l; r < n; r++) {
24                s += balance[r];
25                if (s == 0)
26                    result = Math.max(result, r - l + 1);
27            }
28        }
29
30        return result;
31    }
32}