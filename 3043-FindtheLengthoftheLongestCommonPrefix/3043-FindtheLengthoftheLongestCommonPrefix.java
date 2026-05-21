// Last updated: 5/21/2026, 11:03:11 PM
1class Solution {
2    public int longestCommonPrefix(int[] arr1, int[] arr2) {
3        if (arr1.length > arr2.length) {
4            int[] temp = arr1;
5            arr1 = arr2;
6            arr2 = temp;
7        }
8
9        Set<Integer> prefix_set = new HashSet<>();
10
11        for (int n: arr1) {
12            while (n > 0 && !prefix_set.contains(n)){
13                prefix_set.add(n);
14                n = n / 10;
15            }
16        }
17
18        int res = 0;
19        for (int n: arr2) {
20            while (n > 0 && !prefix_set.contains(n)){
21                n = n / 10;
22            }
23            if (n > 0) {
24                res = Math.max(res, String.valueOf(n).length());
25            }
26            
27        }
28        return res;
29    }
30}