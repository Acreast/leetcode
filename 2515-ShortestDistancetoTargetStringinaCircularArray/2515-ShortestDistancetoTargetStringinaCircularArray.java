// Last updated: 4/15/2026, 9:32:22 PM
1class Solution {
2    public int closestTarget(String[] words, String target, int startIndex) {
3        ArrayList<Integer> occurences = new ArrayList<>();
4
5        int res = Integer.MAX_VALUE;
6        for (int i = 0; i < words.length; i++) {
7            if (target.equals(words[i])) {
8                occurences.add(i);
9            }
10        }
11
12        for (int index : occurences) {
13            int direct = Math.abs(index - startIndex);
14            int wrap = words.length - direct;
15            int dist = Math.min(direct, wrap);
16
17            res = Math.min(res, dist);
18        }
19
20        return (res == Integer.MAX_VALUE) ? -1 : res;
21    }
22}