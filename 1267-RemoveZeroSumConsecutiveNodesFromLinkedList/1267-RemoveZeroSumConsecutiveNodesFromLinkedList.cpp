// Last updated: 7/12/2025, 11:52:48 PM
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
    ListNode* removeZeroSumSublists(ListNode* head) {
        // There is a chance that the head is also detached
        ListNode* dummy = new ListNode(0);
        dummy->next = head;
        // Cache to store the listnodes, for us to detach the linked list
        unordered_map<int, ListNode*> prefixSumToNode;
        int prefixSum = 0;
        for (ListNode* current = dummy; current !=nullptr; current = current->next){
            prefixSum += current->val;
            if(prefixSumToNode.count(prefixSum)){
                ListNode* prev = prefixSumToNode[prefixSum];
                ListNode* toRemove = prev->next;
                int p = prefixSum + (toRemove ? toRemove->val : 0);
                while (p != prefixSum) {
                    prefixSumToNode.erase(p);
                    toRemove = toRemove->next;
                    p += (toRemove? toRemove-> val: 0);
                }
                prev->next = current->next;
            } else {
                prefixSumToNode[prefixSum] = current;
            }
        }
        
        return dummy->next;
    }
};