#include <vector>
#include <iostream>
#include <set>
#include <set>

using namespace std;

class Solution {
public:
    string longestPalindrome(string s) {
        int best_hi = 1;
        int best_lo = 0;
        int curr_hi = 1;
        int curr_lo = 0;
        int streak_length = 1;
        map<char, int> char_for_pali {{s[0], 0}};

        cout << "s    clo   chi" << endl;
        for (int i = 1; i < s.size(); i++) {
            cout << s[i - 1] << "    " << curr_lo << "      " << curr_hi << endl;

            if (s[i] == s[i - 1]) {
                streak_length++;
            } else {
                streak_length = 1;
            }

            if (char_for_pali.find(s[i]) != char_for_pali.end()) {
                curr_hi++;
                curr_lo = char_for_pali[s[i]];
            } else {
                curr_hi = i + 1;
                curr_lo = i;
            }

            if (curr_hi - curr_lo > best_hi - best_lo) {
                best_hi = curr_hi;
                best_lo = curr_lo;
            }

            char_for_pali.clear();

            int streak_start = max(0, i - (streak_length - 1));
            char_for_pali[s[streak_start]] = streak_start;

            int before_streak = max(0, i - streak_length);
            char_for_pali[s[before_streak]] = before_streak;

            int pali_index = curr_lo - 1;
            if (pali_index >= 0) {
                char_for_pali[s[pali_index]] = pali_index;
            }
        }
        cout << s[s.size()-1] << "    " << curr_lo << "      " << curr_hi << endl;

        string pali;
        for (int i = best_lo; i < best_hi; i++) {
            pali.push_back(s[i]);
        }

        return pali;
    }
};

int main() {


  vector<int> t1 {7, 1, 5, 3, 6, 4};
  vector<int> t2 {1, 2, 3, 4, 5};
  vector<int> t3 {7, 6, 4, 3, 1};

  Solution s;

}
