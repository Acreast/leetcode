// Last updated: 2/25/2026, 9:26:45 PM
1class Solution {
2    public int[] sortByBits(int[] arr) {
3        int MAGIC_NUMBER = 10001;
4
5        for (int i = 0; i < arr.length; i ++) {
6            arr[i] += Integer.bitCount(arr[i]) * MAGIC_NUMBER;
7        }
8
9        Arrays.sort(arr);
10
11        for (int i = 0; i < arr.length; i ++) {
12            arr[i] %= MAGIC_NUMBER;
13        }
14
15        return arr;
16    }
17}