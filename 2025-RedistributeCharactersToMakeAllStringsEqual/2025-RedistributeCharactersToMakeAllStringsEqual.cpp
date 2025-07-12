// Last updated: 7/12/2025, 11:48:44 PM
class Solution {
public:
    bool makeEqual(vector<string>& words) {
        // unordered_map<char, int> umap;
        // int arr_length = words.size();

        // for (auto i = 0; i < arr_length ; i++) {
        //     string word = words[i];
        //     for (auto j = 0; j < word.length(); j++) {
        //         char character = word[j];
        //         umap[character] += 1;
        //     }
        // }

        // for (auto char_item : umap) {
        //     if (char_item.second % arr_length > 0) {
        //         return false;
        //     }
        // }
        // return true;

        std::unordered_map<char, int> umap;

        for (const std::string& word : words) {
            for (char character : word) {
                umap[character]++;
            }
        }

        int arr_length = words.size();
        for (const auto& char_item : umap) {
            if (char_item.second % arr_length != 0) {
                return false;
            }
        }

        return true;
        
    }
};