// Last updated: 7/30/2026, 12:29:49 AM
1class Solution {
2    long nCr(int n, int r, int k) {
3        long res = 1; 
4        r = Math.min(r, n - r); // min of r * n - r
5
6        for(int i = 1; i <= r; i++) {
7            res = res * (n - i + 1) / i; 
8            if(res > k) return k + 1; 
9        }
10        return res; 
11    }
12    long ways(int n, int f[], int k) {
13        long total = 1; 
14        for( int i = 0; i < 26; i++) {
15            total *= nCr(n, f[i], k); 
16            if(total > k) return k + 1; // bigger exact doesn't mater 
17            n -= f[i]; 
18        }
19        return total; 
20    }
21    public String smallestPalindrome(String s, int k) {
22        int n = s.length(); 
23        int len = n/2; 
24        int f[] = new int[26]; 
25        for(int i = 0; i < n; i++) f[s.charAt(i) - 'a']++; 
26
27        // half it 
28        char str[] = new char[n]; 
29        for(int i = 0; i < 26; i++) {
30            if(f[i] % 2 == 1) str[n/2] = (char)('a' + i); 
31            f[i] /= 2; 
32        }
33
34        // only half matters 
35        long cnt = ways(len, f, k); 
36
37        if(cnt < k) return ""; // else possible 
38
39        /// first half 
40        for(int idx = 0; idx < len; idx++) {
41            for(int i = 0; i < 26; i++) {
42                if(f[i] == 0) continue; 
43                // pick cur 
44                f[i]--; // reduc freq 
45                long possible = ways(len - idx - 1, f, k); 
46                if(possible >= k) {
47                    // fix cur
48                    str[idx] = (char) ('a' + i); 
49                    break; 
50                } else {
51                    k -= possible; 
52                    f[i]++; // undo it. 
53                } 
54            }
55        }
56
57        // mirror 
58        for(int i = 0; i < len; i++) {
59            str[n - i - 1] = str[i]; 
60        }
61        return String.valueOf(str); 
62    }
63}