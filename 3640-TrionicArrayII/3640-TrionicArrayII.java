// Last updated: 2/6/2026, 12:39:44 AM
1class Solution {
2    public int[] constructTransformedArray(int[] A) {
3        int n = A.length, bias = n * (99 / n) + n;
4        int[] res = new int[n];
5
6        for (int i = 0; i < n; i++)
7            res[i] = A[(i + A[i] + bias) % n];
8
9        return res;
10    }
11}
12