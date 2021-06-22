#include <vector>
#include <iostream>
#include <set>
#include <map>

using namespace std;

class Solution {
public:
    string longestPalindrome(string s) {
        int best_hi = 1;
        int best_lo = 0;
        int curr_hi = 1;
        int curr_lo = 0;

        map<char, set<int>> pali_chars {{s[0], {0}}};

        for (int i = 1; i < s.size(); i++) {

            map<char, set<int>> updated_chars;
            if (pali_chars.find(s[i]) != pali_chars.end()) {
                curr_hi++;
                curr_lo = *pali_chars[s[i]].begin();

                for (auto x : pali_chars[s[i]]) {
                    if (x - 1 >= 0) {
                        updated_chars[s[x - 1]].insert(x - 1);
                    }
                }
            } else {
                curr_hi = i + 1;
                curr_lo = i;
            }

            if (curr_hi - curr_lo > best_hi - best_lo) {
                best_hi = curr_hi;
                best_lo = curr_lo;
            }

            pali_chars.clear();
            pali_chars = updated_chars;
            pali_chars[s[i]].insert(i);
            pali_chars[s[i - 1]].insert(i - 1);

            int pali_index = curr_lo - 1;
            if (pali_index >= 0) {
                pali_chars[s[pali_index]].insert(pali_index);
            }
        }

        string pali;
        for (int i = best_lo; i < best_hi; i++) {
            pali.push_back(s[i]);
        }

        return pali;
    }
};

int main() {

    Solution s;
    cout << s.longestPalindrome("aaaaa") << endl;
}
