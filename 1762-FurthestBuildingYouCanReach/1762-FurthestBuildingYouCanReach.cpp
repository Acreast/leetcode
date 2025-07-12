// Last updated: 7/12/2025, 11:49:56 PM
class Solution {
public:
    int furthestBuilding(vector<int>& heights, int bricks, int ladders) {
        priority_queue<int> maxheap;

        for (auto i = 0 ; i < heights.size()-1; i++) {
            int diff = heights[i + 1] - heights[i];
            if (diff <= 0) {
                continue;
            }
            bricks -= diff;
            maxheap.push(diff);

            if ( bricks < 0 ) {
                if (ladders == 0) {
                    return i;
                }
                ladders -= 1;
                bricks += maxheap.top();
                maxheap.pop();
            }
        }
        return heights.size() - 1;
    }
};