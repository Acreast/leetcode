// Last updated: 7/12/2025, 11:49:54 PM
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
    ListNode* mergeInBetween(ListNode* list1, int a, int b, ListNode* list2) {
        ListNode* curr = list1;
        int ptr = 0;
        while (ptr < a -1) {
            curr = curr->next;
            ptr +=1;
        }

        ListNode* head = curr;

        while(ptr <= b){
            curr = curr->next;
            ptr +=1;
        }

        head->next = list2;
        while(list2->next != nullptr){
            list2 = list2->next;
        }
        list2->next = curr;
        return list1;
    }
};