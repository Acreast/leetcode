// Last updated: 4/7/2026, 10:45:34 PM
1class Robot {
2    public int w, h;
3    public int x, y;
4    public int dir;
5    public int perimeter;
6
7    public int[][] directions = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
8
9    public String[] dirNames = {"East", "North", "West", "South"};
10
11    public Robot(int width, int height) {
12        w = width;
13        h = height;
14        x = 0;
15        y = 0;
16        dir = 0;
17        perimeter = 2 * (w + h - 2);
18    }
19    
20    public void step(int num) {
21        if (perimeter == 0) return;
22
23        num %= perimeter;
24        if (num == 0) num = perimeter;
25
26        while (num-- > 0) {
27            int nx = x + directions[dir][0];
28            int ny = y + directions[dir][1];
29
30            if (nx < 0 || nx >= w || ny < 0 || ny >= h) {
31                dir = (dir + 1) % 4;
32                nx = x + directions[dir][0];
33                ny = y + directions[dir][1];
34            }
35
36            x = nx;
37            y = ny;
38        }
39    }
40    
41    public int[] getPos() {
42        return new int[]{x ,y};
43    }
44    
45    public String getDir() {
46        return dirNames[dir];
47    }
48}
49
50/**
51 * Your Robot object will be instantiated and called as such:
52 * Robot obj = new Robot(width, height);
53 * obj.step(num);
54 * int[] param_2 = obj.getPos();
55 * String param_3 = obj.getDir();
56 */