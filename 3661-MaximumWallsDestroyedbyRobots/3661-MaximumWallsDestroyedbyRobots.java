// Last updated: 4/4/2026, 1:17:57 AM
1class Solution {
2    class Robot {
3        int pos;
4        int dist;
5        Robot(int pos, int dist) {
6            this.pos = pos;
7            this.dist = dist;
8        }
9    }
10
11    public int maxWalls(int[] robots, int[] distance, int[] walls) {
12        int n = robots.length;
13        Robot[] r_arr = new Robot[n];
14        for (int i = 0; i < n; i ++) {
15            r_arr[i] = new Robot(robots[i],distance[i]);
16        }
17
18        Arrays.sort(r_arr, (a,b) -> Integer.compare(a.pos, b.pos));
19        Arrays.sort(walls);
20
21        int[] left_count = new int[n];
22        int[] right_count  = new int[n];
23        int[] common = new int[n];
24
25        for (int i = 0; i < n; i ++) {
26            Robot r = r_arr[i];
27            int left_start = r.pos - r.dist;
28            if (i > 0) {
29                left_start = Math.max(left_start, r_arr[i - 1].pos + 1);
30            }
31            int left_end = r.pos;
32            int left_idx_start= lower_bound(walls, left_start);
33            int left_idx_end = upper_bound(walls, left_end) - 1;
34
35            if (left_idx_start <= left_idx_end) {
36                left_count[i] = left_idx_end - left_idx_start + 1;
37            } else {
38                left_count[i] = 0;
39            }
40            int right_start = r.pos;
41            int right_end = r.pos + r.dist;
42            if (i < n - 1) {
43                right_end = Math.min(right_end, r_arr[i + 1].pos - 1);
44            }
45            int right_idx_start = lower_bound(walls, right_start);
46            int right_idx_end = upper_bound(walls, right_end) - 1;
47            right_count[i] = (right_idx_start <= right_idx_end) ? right_idx_end - right_idx_start + 1 : 0;
48        }
49        for (int i = 1; i < n; i++) {
50            Robot prev = r_arr[i-1];
51            Robot curr = r_arr[i];
52            int prev_right_start = prev.pos;
53            int prev_right_end = prev.pos + prev.dist;
54            prev_right_end = Math.min(prev_right_end, curr.pos - 1);
55            int curr_left_start = curr.pos - curr.dist;
56            curr_left_start = Math.max(curr_left_start, prev.pos + 1);
57            int curr_left_end = curr.pos;
58            int common_start = Math.max(prev_right_start, curr_left_start);
59            int common_end = Math.min(prev_right_end, curr_left_end);
60            if (common_start <= common_end) {
61                int common_idx_start = lower_bound(walls, common_start);
62                int common_idx_end = upper_bound(walls, common_end) - 1;
63                if (common_idx_start <= common_idx_end) {
64                    common[i] = common_idx_end - common_idx_start + 1;
65                }
66            }
67        }
68        int[] dp_left = new int[n];
69        int[] dp_right = new int[n];
70        dp_left[0] = left_count[0];
71        dp_right[0] = right_count[0];
72        for (int i = 1; i < n; i++) {
73            dp_left[i] = left_count[i] + Math.max(dp_left[i-1], dp_right[i-1] - common[i]);
74            dp_right[i] = right_count[i] + Math.max(dp_left[i-1], dp_right[i-1]);
75        }
76        return Math.max(dp_left[n-1], dp_right[n-1]);
77    }
78
79    private int lower_bound(int[] walls, int target) {
80        int low = 0, high = walls.length;
81        while (low < high) {
82            int mid = (low + high) / 2;
83            if (walls[mid] < target) low = mid + 1;
84            else high = mid;
85        }
86        return low;
87    }
88
89    private int upper_bound(int[] walls, int target) {
90        int low = 0, high = walls.length;
91        while (low < high) {
92            int mid = (low + high) / 2;
93            if (walls[mid] <= target) low = mid + 1;
94            else high = mid;
95        }
96        return low;
97    }
98
99}