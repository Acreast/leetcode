// https://leetcode.com/problems/design-hashmap/description/?envType=daily-question&envId=2023-10-04


#include <iostream>     // std::cout
#include <algorithm>    // std::fill
#include <vector>  

class MyHashMap {
public:
    int data[1000001];
    MyHashMap() {
        std::fill(data, data + 1000000, -1);
    }
    
    void put(int key, int value) {
        data[key] = value;
    }
    
    int get(int key) {
        return data[key];
    }
    
    void remove(int key) {
        data[key] = -1;
    }
};

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap* obj = new MyHashMap();
 * obj->put(key,value);
 * int param_2 = obj->get(key);
 * obj->remove(key);
 */