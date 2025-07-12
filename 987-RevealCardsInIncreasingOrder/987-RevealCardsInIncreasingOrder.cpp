// Last updated: 7/12/2025, 11:53:56 PM
class Solution {
public:
    vector<int> deckRevealedIncreasing(vector<int>& deck) {
        std::sort(deck.begin(),deck.end());
        
        int size = deck.size();
        deque<int> deck_queue;
        vector<int> result(size);
        for (int i = 0; i < size; i++) {
            deck_queue.push_back(i);
        }

        for (int card:deck){
            int index = deck_queue.front();
            deck_queue.pop_front();
            result[index] = card;
            if (!deck_queue.empty()){
                deck_queue.push_back(deck_queue.front());
                deck_queue.pop_front();
            }
        }
        return result;
    }
};