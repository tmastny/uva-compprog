#include <vector>
#include <map>
#include <iostream>

using namespace std;

// I see two potential solutions:

// 1. create a frequency map. This is 0(n) time,
//    with 0(n) memory for the map


// 2. sort the array, and with a temporary index
//    counting the same letters in sequence.
//    This requires 0(1) memory, but O(nlogn) time.
//    ^ this doesn't work, because it's not the
//    *only* unique number, just the first.

// I don't think there is a constant memory solution.
// You either:
//      1. as you search through the array, you don't
//         know if a letter is unique until you look through every letter
//      2. then you need to go back and find the first unique letter,
//         so you have to save the frequency of each letter.

class Solution {
public:
    int firstUniqChar(string s) {
        map<char, int> freq;
        for (auto c : s) {
            if (freq.find(c) == freq.end()) {
                freq[c] = 0;
            }
            freq[c]++;
        }

        for (int i = 0; i < s.size(); i++) {
            if (freq[s[i]] == 1) {
                return i;
            }
        }

        return -1;
    }
};


int main() {

}
