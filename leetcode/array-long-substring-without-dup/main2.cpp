#include <vector>
#include <iostream>
#include <unordered_map>

using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if (s == "") return 0;

        unordered_map<char,int> char_indices;
        int curr_lo = 0;
        int curr_hi = 0;
        int best_lo = 0;
        int best_hi = 0;

        for (int i = 0; i < s.size(); i++) {

            // index the current element if it is new
            // or it is below last next_lo
            if (char_indices.find(s[i]) == char_indices.end() || char_indices[s[i]] < curr_lo) {
                char_indices[s[i]] = i;
                curr_hi++;

            } else {

                curr_lo = char_indices[s[i]] + 1;
                curr_hi = i + 1;


                char_indices[s[i]] = i;
            }

            if (curr_hi - curr_lo > best_hi - best_lo) {
                best_hi = curr_hi;
                best_lo = curr_lo;
            }
        }

        return best_hi - best_lo;
    }
};

int main() {


  vector<int> t1 {7, 1, 5, 3, 6, 4};
  vector<int> t2 {1, 2, 3, 4, 5};
  vector<int> t3 {7, 6, 4, 3, 1};

  Solution s;
}
