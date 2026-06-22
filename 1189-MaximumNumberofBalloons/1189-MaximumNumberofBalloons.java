// Last updated: 6/22/2026, 11:24:35 PM
1class Solution {
2    public int maxNumberOfBalloons(String text) {
3        HashMap<Character, Integer> dict = new HashMap<Character, Integer>();
4
5        for (char c:text.toCharArray()) {
6            if (c == 'a' || c == 'b' || c == 'l' || c == 'o' || c == 'n')
7                dict.put(c, dict.getOrDefault(c, 0) + 1);
8        }
9        int res = Integer.MAX_VALUE;    
10        char[] target = {'a', 'b', 'l', 'o', 'n'};
11        for (char c: target) {
12            if (c == 'l' || c == 'o') {
13                res = Math.min(res, dict.getOrDefault(c,0) / 2);
14            }
15            else {
16                res = Math.min(res, dict.getOrDefault(c,0));
17            }
18        }
19
20        return res;
21    }
22}