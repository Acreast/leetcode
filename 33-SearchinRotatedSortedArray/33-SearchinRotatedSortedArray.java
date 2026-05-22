// Last updated: 5/23/2026, 1:08:47 AM
1class Solution {
2    public int search(int[] A, int target) {
3        int l = 0;
4        int r = A.length - 1;
5        int n = A.length;
6        if (n == 0) {
7            return - 1;
8        }
9        while (l <= r) {
10            int mid = l + (r - l) / 2;
11            if (A[mid] == target) {
12                return mid;
13            }
14
15            if (A[mid] >= A[l]) {
16                if (A[l] <= target && target < A[mid]) {
17                    r = mid - 1;
18                } else {
19                    l = mid + 1;
20                }
21               
22            } else {
23                if (A[mid] < target && target <= A[r]) {
24                    l = mid + 1;
25                } else {
26                    r = mid - 1;
27                }
28            }
29
30
31
32        }
33
34        return - 1;
35    }
36}