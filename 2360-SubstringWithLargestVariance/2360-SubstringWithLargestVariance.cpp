// Last updated: 7/12/2025, 11:46:55 PM
class Solution {
public:
   int largestVariance(string s)
   {
        int n = s.size();
        unordered_set<char>Set(s.begin(), s.end());

        int ret = 0;
        for (char a: Set)
        {
            for(char b: Set)
            {
                if(a==b) continue;
                int dp0 = 0, dp1 = INT_MIN/2;
                
                for (int i =0 ; i<n; i++)
                {
                    if (s[i] == a)
                    {
                        dp1 = dp1 + 1;
                        dp0 = dp0 + 1;
                    }
                    else if (s[i] == b)
                    {
                        dp1 = max(dp0 - 1, dp1 -1 );
                        dp0 = 0;
                    }

                    ret = max(ret, dp1);
                }
            }
        }
        return ret;
    }
};