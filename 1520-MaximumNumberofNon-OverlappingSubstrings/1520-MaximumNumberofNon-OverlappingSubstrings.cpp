// Last updated: 9/19/2026, 1:38:28 AM
1class Solution {
2public:
3    vector<string> maxNumOfSubstrings(string s) {
4        int count[26] = {};
5        int first[26], last[26];
6
7        fill(first, first + 26, -1);
8        fill(last, last + 26, -1);
9
10        vector<int> order;
11
12        for (int i = 0; i < s.size(); i++) {
13            int c = s[i] - 'a';
14
15            if (count[c] == 0) {
16                first[c] = i;
17                order.push_back(c);
18            }
19
20            count[c]++;
21            last[c] = i;
22        }
23
24        vector<string> res;
25        deque<array<int, 3>> queue;
26
27        for (int c : order) {
28            queue.push_front({first[c], last[c], count[c]});
29
30            int left = INT_MAX;
31            int right = INT_MIN;
32            int total = 0;
33
34            for (auto& item : queue) {
35                total += item[2];
36                left = min(left, item[0]);
37                right = max(right, item[1]);
38
39                if (total == right - left + 1) {
40                    break;
41                }
42            }
43
44            if (total == right - left + 1) {
45                res.push_back(s.substr(left, right - left + 1));
46                queue.clear();
47            }
48        }
49
50        return res;
51    }
52};