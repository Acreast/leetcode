// Last updated: 7/12/2025, 11:48:14 PM
class Solution {
public:
    string reversePrefix(string word, char ch) {
        stack<char> current_stack;
        string result = "";
        int stopped_index = 0;
        for(int i = 0; i < word.length(); i ++){
            if (word[i] == ch) {
                current_stack.push(word[i]);
                stopped_index += 1;
                break;
            }
            if (i == word.length() -1) {
                result = word;
                stack<char> empty_stack;
                current_stack = empty_stack;
                break;
            }
            current_stack.push(word[i]);
            stopped_index += 1;
        }

        if (!current_stack.empty()){
            while (!current_stack.empty()) {
                result += current_stack.top();
                current_stack.pop();
            }
            for (int i = stopped_index; i < word.length() ; i ++) {
                result += word[i];
            }
        } else {
            result = word;
        }

        return result;


    }
};