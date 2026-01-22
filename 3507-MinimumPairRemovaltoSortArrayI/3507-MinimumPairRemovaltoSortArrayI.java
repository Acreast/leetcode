// Last updated: 1/23/2026, 12:29:27 AM
1class Solution {
2    public int minPair(List<Integer> v) {
3        int minSum = (int)1e9;
4        int pos = -1;
5
6        for (int i = 0; i < v.size() - 1; i ++) {
7            int sum = v.get(i) + v.get(i + 1);
8            if (sum < minSum) {
9                minSum = sum;
10                pos = i;
11            }
12        }
13        return pos;
14    }
15
16    public void mergePairs(List<Integer> v , int pos) {
17        v.set(pos, v.get(pos) + v.get(pos + 1));
18        v.remove(pos + 1);
19    }
20
21    public int minimumPairRemoval(int[] nums) {
22        List<Integer> v = new ArrayList<>();
23        for (int x : nums) v.add(x);
24        int count = 0;
25        while(!isSorted(v)) {
26            int pos = minPair(v);
27            mergePairs(v, pos);
28            count += 1;
29        }
30        return count;
31    }
32
33    private boolean isSorted(List <Integer> v) {
34        for (int i = 0; i < v.size() - 1; i ++) {
35            if(v.get(i) > v.get(i + 1)) return false;
36        } 
37        return true;
38    }
39   
40}