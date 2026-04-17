// Last updated: 4/18/2026, 12:04:48 AM
1class Solution {
2    public int minMirrorPairDistance(int[] nums) {
3        int minDist = Integer.MAX_VALUE;
4        Map<Integer, Integer> map = new HashMap<>();
5        int i = 0;
6        for (int n : nums) {
7            if (map.containsKey(n)) {
8                minDist = Math.min(minDist, i - map.get(n));
9            }
10            int rev = reverse(n);
11            map.put(rev, i);
12            i++;
13        }
14        return minDist == Integer.MAX_VALUE ? -1 : minDist;
15    }
16    
17    private static int reverse(int num) {
18        int rev = 0;
19        while (num > 0) {
20            rev = rev * 10 + num % 10;
21            num /= 10;
22        }
23        return rev;
24    }
25
26}