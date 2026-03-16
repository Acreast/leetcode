// Last updated: 3/17/2026, 12:41:58 AM
1class Solution {
2public:
3    vector<int> getBiggestThree(vector<vector<int>>& grid) {
4        int n=grid.size(),m=grid[0].size();
5        set<int>uniqueSum;
6        for(int i=0;i<n;i++){
7            for(int j=0;j<m;j++){
8                uniqueSum.insert(grid[i][j]);
9                for(int len=1;i+2*len<n && j-len>=0 && j+len<m;len++){
10                    int currentSum=0;
11                    for(int ind=0;ind<len;ind++)currentSum+=grid[i+ind][j+ind]; 
12                    for(int ind=0;ind<len;ind++)currentSum+=grid[i+len+ind][j+len-ind];
13                    for(int ind=0;ind<len;ind++)currentSum+=grid[i+2*len-ind][j-ind];
14                    for(int ind=0;ind<len;ind++)currentSum+=grid[i+len-ind][j-len+ind];
15                    uniqueSum.insert(currentSum);
16                }
17   
18            }
19        }
20        vector<int>ans(uniqueSum.rbegin(),uniqueSum.rend());
21        if(ans.size()>3)ans.resize(3);
22        return ans;
23    }
24};