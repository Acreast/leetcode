// Last updated: 1/24/2026, 12:38:38 AM
1class Solution {
2    private static class Segment implements Comparable<Segment> {
3        int index;
4        long value;
5        long mergeCost;
6        Segment left;
7        Segment right;
8
9        Segment(int idx, long val) {
10            index = idx;
11            value = val;
12        }
13
14        @Override
15        public int compareTo(Segment o) {
16            if (right == null || o.right == null) {
17                return right == null ? 1 : -1;
18            }
19            long diff = mergeCost - o.mergeCost;
20            if (diff != 0) return diff < 0 ? -1 : 1;
21            return index - o.index;
22        }
23    }
24    
25    public int minimumPairRemoval(int[] nums) {
26        TreeSet<Segment> heap = new TreeSet<>();
27        int violations = 0;
28
29        Segment current = null;
30
31        for (int i = 0; i < nums.length; i++) {
32            Segment node = new Segment(i, nums[i]);
33
34            if (current != null) {
35                if (node.value < current.value) violations++;
36
37                current.right = node;
38                node.left = current;
39
40                current.mergeCost = current.value + node.value;
41                heap.add(current);
42            }
43            current = node;
44        }
45
46        heap.add(current);
47
48        int operations = 0;
49
50        while (violations > 0) {
51            operations++;
52
53            Segment best = heap.pollFirst();
54            Segment next = best.right;
55
56            if (next.value < best.value) violations--;
57
58            best.value += next.value;
59            best.mergeCost = best.value + (next.right != null ? next.right.value : 0);
60
61            best.right = next.right;
62            if (next.right != null) {
63                if (next.right.value < next.value) violations--;
64                next.right.left = best;
65                if (best.value > next.right.value) violations++;
66            }
67
68            heap.remove(next);
69            heap.add(best);
70
71            Segment prev = best.left;
72            if (prev != null) {
73                heap.remove(prev);
74
75                if (prev.value > prev.mergeCost - prev.value) violations--;
76                if (prev.value > best.value) violations++;
77
78                prev.mergeCost = prev.value + best.value;
79                prev.right = best;
80
81                heap.add(prev);
82            }
83        }
84
85        return operations;
86    }
87}
88