// Last updated: 1/27/2026, 12:03:36 AM
1class Solution {
2    public List<List<Integer>> minimumAbsDifference(int[] arr) {
3        Arrays.sort(arr);
4        int n = arr.length;
5        int minDiff = Integer.MAX_VALUE;
6        List<List<Integer>> res = new ArrayList<>();
7
8        for (int i = 1; i < n; i ++) {
9            int diff = arr[i] - arr[i - 1];
10            if (diff < minDiff) {
11                minDiff = diff;
12                res = new ArrayList<>();
13                res.add(Arrays.asList(arr[i -1], arr[i]));
14            } else if (diff == minDiff) {
15                res.add(Arrays.asList(arr[i -1], arr[i]));
16            }
17        }
18
19        return res;
20    }
21}