// Last updated: 6/4/2026, 11:30:08 PM
1class Solution {
2    public int totalWaviness(int num1, int num2) {
3        int res = 0;
4        for (int i = num1; i <= num2; i ++) {
5            int temp = i;
6            int prev = temp % 10;
7            temp /= 10;
8            while (temp >= 10) {
9                int curr = temp % 10;
10                int next = (temp/10) % 10;
11                if (curr > prev && curr > next) 
12                    res ++;
13                else if (curr < prev && curr < next)
14                    res ++;
15
16                prev = curr;
17                temp /= 10;
18            }
19        }
20
21        return res;
22    }
23}