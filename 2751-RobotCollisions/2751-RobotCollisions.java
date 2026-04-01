// Last updated: 4/1/2026, 11:24:40 PM
1class Solution {
2    class Robot {
3        int pos;
4        char dir;
5        int health;
6        int orig_i;
7
8        Robot(int pos, char dir, int health, int orig_i) {
9            this.pos = pos;
10            this.dir = dir;
11            this.health = health;
12            this.orig_i = orig_i;
13        }
14
15
16    }
17    
18    public List<Integer> survivedRobotsHealths(int[] positions, int[] healths, String directions) {
19        int n = positions.length;
20        Robot [] robots = new Robot[n];
21        
22        for (int i = 0; i < n; i ++) {
23            robots[i] = new Robot(
24                positions[i],
25                directions.charAt(i),
26                healths[i],
27                i
28            );
29        }
30
31        Arrays.sort(robots, (a,b) -> Integer.compare(a.pos, b.pos));
32        Stack<Robot> stack = new Stack<>();
33
34        for (Robot curr : robots) {
35            while (!stack.isEmpty() && curr.dir == 'L' && stack.peek().dir == 'R') {
36                Robot top = stack.peek();
37
38                if (top.health > curr.health) {
39                    top.health -= 1;
40                    curr.health = 0;
41                    break;
42                } else if (top.health < curr.health) {
43                    stack.pop();
44                    curr.health -= 1;
45                } else {
46                    stack.pop();
47                    curr.health = 0;
48                    break;
49                }
50            }
51
52            if (curr.health > 0) {
53                stack.push(curr);
54            }
55        }
56
57        stack.sort((a,b) -> Integer.compare(a.orig_i, b.orig_i));
58
59        List<Integer> res = new ArrayList<>();
60        for (Robot r: stack) {
61            res.add(r.health);
62        }
63
64        return res;
65    }
66}