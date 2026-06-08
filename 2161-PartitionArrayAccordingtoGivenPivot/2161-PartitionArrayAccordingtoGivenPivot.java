// Last updated: 6/8/2026, 10:55:34 PM
1class Solution {
2    public int[] pivotArray(int[] nums, int pivot) {
3        List<Integer> leftPartition = new ArrayList<>();
4        List<Integer> middlePartition = new ArrayList<>();
5        List<Integer> rightPartition = new ArrayList<>();
6
7        for(int i = 0; i < nums.length; i ++) {
8            int cur = nums[i];
9            if (cur == pivot) 
10                middlePartition.add(cur);
11            else if (cur < pivot)
12                leftPartition.add(cur);
13            else
14                rightPartition.add(cur);
15        }
16
17        int[] res = Stream.of(leftPartition, middlePartition, rightPartition)
18                        .flatMap(List::stream)
19                        .mapToInt(Integer::intValue)
20                        .toArray();
21        return res;
22        
23    }
24}