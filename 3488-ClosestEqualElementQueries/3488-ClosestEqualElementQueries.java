// Last updated: 4/17/2026, 12:06:20 AM
1class Solution {
2    public List<Integer> solveQueries(int[] nums, int[] queries) {
3        Map<Integer, List<Integer>> map = new HashMap<>();
4        List<Integer> res = new ArrayList<>();
5        int n = nums.length;
6
7        for (int i = 0; i < n;i ++) {
8            List<Integer> list = map.getOrDefault(nums[i], new ArrayList<>());
9            list.add(i);
10            map.put(nums[i],list);
11        }
12
13
14        for (int i = 0; i < queries.length; i ++) {
15            int queryIndex = queries[i];
16            int targetValue = nums[queryIndex];
17            List<Integer> indices = map.get(targetValue);
18
19            if (indices.size() == 1) {
20                res.add(-1);
21                continue;
22            }
23
24            int pos = binSearch(indices,queryIndex);
25            int size = indices.size();
26
27            int prevIndex = indices.get((pos - 1 + size) % size);
28            int nextIndex = indices.get((pos + 1) % size);
29
30            int distPrev = Math.min(Math.abs(queryIndex - prevIndex),
31                                    n - Math.abs(queryIndex - prevIndex));
32            int distNext = Math.min(Math.abs(queryIndex - nextIndex),
33                                    n - Math.abs(queryIndex - nextIndex));
34
35            res.add(Math.min(distPrev,distNext));
36        }
37
38        return res;
39    }
40
41    private int binSearch(List<Integer> list, int target) {
42        int left = 0, right = list.size() - 1;
43        while (left <= right) {
44            int mid = left + (right - left) / 2;
45            int midVal = list.get(mid);
46            if(midVal == target) {
47                return mid;
48            } else if (midVal < target) {
49                left = mid + 1;
50            } else {
51                right = mid - 1;
52            }
53        }
54        return -1;
55    }
56}