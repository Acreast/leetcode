// Last updated: 7/12/2025, 11:50:23 PM
class Solution {
public:
    int numSpecial(std::vector<std::vector<int>>& mat) {
        int specials = 0;

        for (int i = 0; i < mat.size(); i++) {
            int index = checkRow(mat, i);
            if (index >= 0 && checkColumn(mat, i, index))
                specials++;
        }

        return specials;
    }

private:
    int checkRow(std::vector<std::vector<int>>& mat, int i) {
        int index = -1;
        for (int j = 0; j < mat[0].size(); j++) {
            if (mat[i][j] == 1) {
                if (index >= 0)
                    return -1;
                else
                    index = j;
            }
        }
        return index;
    }

    bool checkColumn(std::vector<std::vector<int>>& mat, int i, int index) {
        for (int j = 0; j < mat.size(); j++) {
            if (mat[j][index] == 1 && j != i)
                return false;
        }
        return true;
    }
};