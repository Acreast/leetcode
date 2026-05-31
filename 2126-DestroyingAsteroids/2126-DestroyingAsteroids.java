// Last updated: 6/1/2026, 12:12:57 AM
1class Solution {
2    public boolean asteroidsDestroyed(int mass, int[] asteroids) {
3        Arrays.sort(asteroids);
4        long cur_mass = mass;
5        for (int i = 0; i < asteroids.length; i ++) {
6            if (asteroids[i] > cur_mass) {
7                return false;
8            } else {
9                cur_mass += asteroids[i];
10            }
11        } 
12
13        return true;
14    }
15}