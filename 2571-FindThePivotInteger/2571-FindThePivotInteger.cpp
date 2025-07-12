// Last updated: 7/12/2025, 11:45:46 PM
class Solution {
public:
    int pivotInteger(int n) {
        int sum = n * (n + 1) / 2;
        double a = sqrt(sum);

        if (a - ceil(a) == 0)
            return int(a);
        else
            return -1;
    }
};