// Last updated: 7/12/2025, 11:44:43 PM
class Solution {
public:
int buyChoco(vector<int>& prices, int money) {
        int firstMinCost = INT_MAX;
        int secondMinCost = INT_MAX;

        for (int p : prices) {
            if (p < firstMinCost) {
                secondMinCost = firstMinCost;
                firstMinCost = p;
            } else {
                secondMinCost = min(secondMinCost, p);
            }
        }

        int leftover = money - (firstMinCost + secondMinCost);

        return leftover >= 0 ? leftover : money;        
    }
};