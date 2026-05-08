// Last updated: 5/9/2026, 12:29:16 AM
1class Solution {
2    static final int n = 1000005;
3    static boolean[] prime = new boolean[n];
4
5    static {
6        prime[0] = prime[1] = true;
7
8        for (int i = 2; i <= 1000; i++)
9            if (!prime[i])
10                for (int j = i * i; j < n; j += i)
11                    prime[j] = true;
12    }
13
14    public int minJumps(int[] nums) {
15        int n = nums.length;
16        int max = nums[0];
17        
18        for (int i = 1; i < n; i++)
19            max = Math.max(max, nums[i]);
20
21        int[] head = new int[max + 1];
22        Arrays.fill(head, -1);
23        int[] next = new int[n];
24
25        for (int i = 0; i < n; i++) {
26            next[i] = head[nums[i]];
27            head[nums[i]] = i;
28        }
29
30        int[] dp = new int[n];
31        Arrays.fill(dp, -1);
32        dp[0] = 0;
33
34        Queue<Integer> queue = new LinkedList<>();
35        queue.add(0);
36
37        Set<Integer> seen = new HashSet<>();
38
39        while (!queue.isEmpty()) {
40            int dq = queue.poll();
41
42            if (dq == n - 1)
43                return dp[dq];
44
45            int right = dq + 1;
46            if (right < n && dp[right] == -1) {
47                dp[right] = dp[dq] + 1;
48                queue.add(right);
49            }
50
51            int left = dq - 1;
52            if (left >= 0 && dp[left] == -1) {
53                dp[left] = dp[dq] + 1;
54                queue.add(left);
55            }
56
57            int val = nums[dq];
58            if (!prime[val] && !seen.contains(val)) {
59                seen.add(val);
60                for (int i = val; i <= max; i += val) {
61                    for (int j = head[i]; j != -1; j = next[j]) {
62                        if (dp[j] == -1) {
63                            dp[j] = dp[dq] + 1;
64                            queue.add(j);
65                        }
66                    }
67                    head[i] = -1;
68                }
69            }
70        }
71
72        return -1;
73    }
74}