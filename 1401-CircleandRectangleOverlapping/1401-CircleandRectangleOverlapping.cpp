// Last updated: 9/20/2026, 1:10:13 AM
1class Solution {
2public:
3    bool checkOverlap(int r, int cx, int cy, int x1, int y1, int x2, int y2) {
4        int x = clamp(cx, x1, x2) - cx;
5        int y = clamp(cy, y1, y2) - cy;
6
7        return x * x + y * y <= r * r;
8    }
9};