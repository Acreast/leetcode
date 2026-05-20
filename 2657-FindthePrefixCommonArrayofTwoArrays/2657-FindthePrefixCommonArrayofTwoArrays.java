// Last updated: 5/21/2026, 12:15:12 AM
1class Solution {
2    public int[] findThePrefixCommonArray(int[] A, int[] B) {
3        int n = A.length;
4        int[] seen = new int[n + 1];
5        Arrays.fill(seen, 0);
6        int common = 0;
7        List<Integer> res = new ArrayList<>();
8        for (int i = 0; i < n; i ++) {
9            if (seen[A[i]] == 0)
10                seen[A[i]] = 1;
11            else if (seen[A[i]] == 1)
12                common++;
13
14            if (seen[B[i]] == 0)
15                seen[B[i]] = 1;
16            else if (seen[B[i]] == 1)
17                common++;
18
19            res.add(common);
20
21        } 
22        return res.stream().mapToInt(i -> i).toArray();
23
24    }
25}