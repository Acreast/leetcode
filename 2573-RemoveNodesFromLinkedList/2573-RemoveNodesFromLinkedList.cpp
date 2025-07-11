// Last updated: 7/12/2025, 11:45:43 PM
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeNodes(ListNode* head) {
        stack<ListNode*> stack;
        ListNode* cur = head;

        while(cur!= nullptr) {
            while(!stack.empty() && stack.top()->val < cur->val){
                stack.pop();
            }
            stack.push(cur);
            cur = cur->next;
        }

        ListNode* nxt = nullptr;
        while(!stack.empty()) {
            cur = stack.top();
            stack.pop();
            cur->next = nxt;
            nxt = cur;
        }

        return cur;
    }
};