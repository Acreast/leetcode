// Last updated: 2/21/2026, 11:45:20 PM
1class Solution {
2    public int countPrimeSetBits(int left, int right) {
3        int count = 0;
4        for (int i = left; i <= right; i ++) {
5            int ones = Integer.bitCount(i);
6            if (isPrime(ones)) {
7                count ++;
8            }
9        }
10        return count;
11
12    }
13
14    public static boolean isPrime(int n) {
15        if (n <= 1) {
16            return false;
17        }
18
19        for (int i = 2; i < n; i ++) {
20            if (n % i == 0) {
21                return false;
22            } 
23        }
24        return true;
25    }
26}