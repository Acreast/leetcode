// Last updated: 5/19/2026, 11:15:00 PM
1class Solution {
2    public int getCommon(int[] nums1, int[] nums2) {
3        int ptr1 = 0, ptr2 = 0;
4
5        while (ptr1 != nums1.length && ptr2 != nums2.length) {
6
7            if (nums1[ptr1] == nums2[ptr2]) {
8                return nums1[ptr1];
9            } else if (nums1[ptr1] > nums2[ptr2]) {
10                ptr2++;
11            } else if (nums1[ptr1] < nums2[ptr2]) {
12                ptr1++;
13            }
14        }
15
16        return -1;
17    }
18}