// Last updated: 1/15/2026, 1:21:45 AM
1class Solution {
2public:
3
4    struct Event {
5        double y;
6        double x1, x2;
7        int type;
8        bool operator<(const Event& other) const {
9            return y < other.y;
10        }
11    };
12
13    struct SegTree {
14        int n;
15        vector<int> cover;
16        vector<double> length;
17        vector<double> xs;
18
19        SegTree(const vector<double>& cords) {
20            xs = cords;
21            n = xs.size() - 1;
22            cover.assign(4 * n, 0);
23            length.assign(4 * n, 0.0);
24        }
25
26        void pushUp(int node, int l, int r) {
27            if(cover[node] > 0) {
28                length[node] = xs[r + 1] - xs[l];
29            } else if ( l == r ) {
30                length[node] = 0.0;
31            } else {
32                length[node] = length[node * 2] + length[node * 2 + 1];
33            }
34        }
35
36        void update(int node, int l, int r, int ql, int qr, int val) {
37            if (ql > r || qr < l) return;
38            if (ql <= l && r <= qr) {
39                cover[node] += val;
40                pushUp(node, l, r);
41                return;
42            }
43            int mid = (l + r) / 2;
44            update(node * 2, l, mid, ql, qr, val);
45            update(node * 2 + 1, mid + 1, r, ql, qr, val);
46            pushUp(node, l, r );
47        }
48
49        double totalCovered() const {
50            return length[1];
51        }
52    };
53
54    double separateSquares(vector<vector<int>>& squares) {
55        vector<Event> events;
56        vector<double> xs;
57
58        for(auto& s: squares) {
59            double x = s[0], y = s[1], len = s[2];
60            events.push_back({y, x, x + len, +1});
61            events.push_back({y + len, x, x + len, -1});
62            xs.push_back(x);
63            xs.push_back(x + len);
64        }
65
66        sort(events.begin(), events.end());
67        sort(xs.begin(), xs.end());
68        xs.erase(unique(xs.begin(), xs.end()), xs.end());
69
70        auto getIndex = [&](double x) {
71            return lower_bound(xs.begin(), xs.end(), x) - xs.begin();
72        };
73
74        SegTree st(xs);
75
76        double totalArea = 0.0;
77        double prevY = events[0].y;
78
79        for (auto& e: events) {
80            double dy = e.y - prevY;
81            totalArea += st.totalCovered() * dy;
82            int l = getIndex(e.x1);
83            int r = getIndex(e.x2) - 1;
84            st.update(1, 0, st.n - 1, l, r, e.type);
85            prevY = e.y;
86        }
87
88        st = SegTree(xs);
89        prevY = events[0].y;
90        double curArea = 0.0;
91        double half = totalArea / 2.0;
92
93        for (auto& e: events) {
94            double dy = e.y - prevY;
95            double bandArea = st.totalCovered() * dy;
96
97            if (curArea + bandArea >= half) {
98                double remaining = half - curArea;
99                return prevY + remaining / st.totalCovered();
100            }
101
102            curArea += bandArea;
103            int l = getIndex(e.x1);
104            int r = getIndex(e.x2) - 1;
105            st.update(1, 0, st.n - 1, l, r, e.type);
106            prevY = e.y;
107        }
108
109        return prevY;
110    }
111};