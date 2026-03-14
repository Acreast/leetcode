// Last updated: 3/15/2026, 12:16:18 AM
1class Solution {
2    public String getHappyString(int n, int k) {
3        return dfs("", n , k, n);
4
5    }
6
7    static String dfs(String prefix, int n, int k, int n2) {
8        if (n == 0) {
9            return prefix;
10        }
11        for (char c : new char[] {'a', 'b', 'c'}) {
12            if (!prefix.isEmpty() && c == prefix.charAt(prefix.length() - 1 )) {
13                continue;
14            }
15            int count = (int) Math.pow(2, n2 - prefix.length() - 1); 
16            if (count >= k) {
17                return dfs(prefix + c, n - 1, k, n2);
18            } else {
19                k -= count;
20            }
21        }
22        return "";
23    }
24}