// Last updated: 3/16/2026, 1:06:22 AM
1class Fancy {
2    private static final int MOD = 1000000007;
3    private ArrayList<Long> val;  
4    private long a, b;  
5    
6    public Fancy() {
7        val = new ArrayList<>();
8        a = 1;
9        b = 0;
10    }
11    
12    public void append(int val) {
13        long x = (val - b + MOD) % MOD;
14        this.val.add((x * modPow(a, MOD - 2, MOD)) % MOD);  
15    }
16    
17    public void addAll(int inc) {
18        b = (b + inc) % MOD;
19    }
20    
21    public void multAll(int m) {
22        a = (a * m) % MOD;
23        b = (b * m) % MOD;
24    }
25    
26    public int getIndex(int idx) {
27        if (idx >= val.size()) return -1; 
28        return (int)((a * val.get(idx) + b) % MOD);
29    }
30
31    private long modPow(long x, long y, long mod) {
32        long res = 1;
33        x = x % mod;
34        while (y > 0) {
35            if (y % 2 == 1) {
36                res = (res * x) % mod;
37            }
38            y = y / 2;
39            x = (x * x) % mod;
40        }
41        return res;
42    }
43}
44
45/**
46 * Your Fancy object will be instantiated and called as such:
47 * Fancy obj = new Fancy();
48 * obj.append(val);
49 * obj.addAll(inc);
50 * obj.multAll(m);
51 * int param_4 = obj.getIndex(idx);
52 */