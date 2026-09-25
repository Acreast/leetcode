// Last updated: 9/26/2026, 1:33:58 AM
1class Solution {
2    set<string> ans;
3
4    void dfs(string s){
5        int r = s.find('}');
6
7        // No braces left
8        if(r == string::npos){
9            ans.insert(s);
10            return;
11        }
12
13        // Find matching '{'
14        int l = s.rfind('{', r);
15
16        string left = s.substr(0, l);
17        string right = s.substr(r + 1);
18
19        // Content inside { }
20        string inside = s.substr(l + 1, r - l - 1);
21
22        string part;
23        stringstream ss(inside);
24
25        while(getline(ss, part, ',')){
26            dfs(left + part + right);
27        }
28    }
29
30public:
31    vector<string> braceExpansionII(string expression) {
32        dfs(expression);
33        return vector<string>(ans.begin(), ans.end());
34    }
35};