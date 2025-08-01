// Last updated: 7/12/2025, 11:49:38 PM
static class DSU {
    vector<int> Parent, Rank;
    public:
    DSU(int n) {
        Parent.resize(n);
        Rank.resize(n, 0);
        for (int i = 0; i < n; i++) Parent[i] = i;
    }
    int Find(int x) {
        return Parent[x] = Parent[x] == x ? x : Find(Parent[x]);
    }
    bool Union(int x, int y) {
        int xset = Find(x), yset = Find(y);
        if (xset != yset) {
            Rank[xset] < Rank[yset] ? Parent[xset] = yset : Parent[yset] = xset;
            Rank[xset] += Rank[xset] == Rank[yset];
            return true;
        }
        return false;
    }
};
class Solution {
public:
    vector<bool> distanceLimitedPathsExist(int n, vector<vector<int>>& edgeList, vector<vector<int>>& queries)
    {
        DSU dsu(n);
		
		//Add query indices to help with organizing/ordering results.
        for(int i=0;i<queries.size();i++)
            queries[i].push_back(i);
		
		//Sort inputs
        sort(queries.begin(), queries.end(), [](auto &l, auto &r) { return l[2] < r[2]; });
        sort(edgeList.begin(), edgeList.end(), [](auto &l, auto &r) { return l.back() < r.back(); });
		
        int i=0;
        vector<bool> result(queries.size());
        for (vector<int> &q:queries) 
        {
			// Two pointer approach. Join the edges till their weight is less than the current query.
            while (i<edgeList.size()&&edgeList[i][2]<q[2]) 
                dsu.Union(edgeList[i][0],edgeList[i++][1]);
			
			//If parents are same we know that their is a path.
            result[q.back()]=dsu.Find(q[0]) == dsu.Find(q[1]);
        }
        return result;
    }
};