// Last updated: 2/21/2026, 12:18:03 AM
1class Solution {
2    public String makeLargestSpecial(String s) {
3        int count = 0, i = 0;
4        List<String> res = new ArrayList<>();
5
6
7        for (int j = 0; j < s.length(); j ++) {
8            if (s.charAt(j) == '1') count ++;
9            else count--;
10
11            if (count == 0) {
12                res.add('1' + makeLargestSpecial(s.substring(i +1, j)) + '0');
13                i = j + 1;
14            }
15        }
16
17        Collections.sort(res, Collections.reverseOrder());
18        return String.join("",res);
19    }
20}