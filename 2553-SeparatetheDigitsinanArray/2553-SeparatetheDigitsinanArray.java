// Last updated: 5/11/2026, 10:20:46 PM
1class Solution {
2    public int[] separateDigits(int[] nums) {
3        List<Integer> temp = new ArrayList<>();
4        for (int n: nums) {
5            String n_str = Integer.toString(n);
6            for (char c: n_str.toCharArray()) {
7                temp.add(Character.getNumericValue(c));
8            }
9        }
10        return temp.stream().mapToInt(Integer::intValue).toArray();
11    }
12}