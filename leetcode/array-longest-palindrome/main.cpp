#include <vector>
#include <iostream>
#include <set>

using namespace std;

class Solution {
private:
    string longest_streak(string s) {
        char max_letter = s[0];
        int max_streak = 1;
        int streak = 1;

        for (int i = 1; i < s.size(); i++) {
            if (s[i] == s[i - 1]) {
                streak++;
                if (streak > max_streak) {
                    max_streak = streak;
                    max_letter = s[i];
                }
            } else {
                streak = 1;
            }
        }

        string longest;
        for (int i = 0; i < max_streak; i++) {
            longest.push_back(max_letter);
        }
        return longest;
    }

public:
    string longestPalindrome(string s) {
        int best_hi = 1;
        int best_lo = 0;
        int curr_hi = 1;
        int curr_lo = 0;

        bool is_single_char = true;

        //cout << endl << "next" << endl;
        for (int i = 1; i < s.size(); i++) {


            //cout << "clo: " << curr_lo << " chi: " << curr_hi << endl;
            if (is_single_char && s[i] == s[curr_lo]) {
                curr_hi = i + 1;

            } else {
                is_single_char = false;

                int temp_lo = curr_lo - 1;
                if (temp_lo >= 0 && s[i] == s[temp_lo]) {
                    curr_hi = i + 1;
                    curr_lo = temp_lo;

                } else if (s[i] == s[i - 1]) {
                    curr_hi = i + 1;
                    curr_lo = i - 1;

                } else {
                    curr_hi = i + 1;
                    curr_lo = i;
                }


                if (curr_hi - curr_lo > best_hi - best_lo) {
                    best_hi = curr_hi;
                    best_lo = curr_lo;
                }
            }
        }
        //cout << "clo: " << curr_lo << " chi: " << curr_hi << endl;

        string pali;
        for (int i = best_lo; i < best_hi; i++) {
            pali.push_back(s[i]);
        }
        // string streak = longest_streak(s);
        // return streak.size() > pali.size() ? streak : pali;
        return pali;
    }
};

/*
"babaaba"
01234567
b         clo: 0 chi: 1
ba        clo: 1 chi: 2
bab       clo: 0 chi: 3
baba      clo: 1 chi: 4
babaa     clo: 4 chi: 5
babaab    clo: 5 chi: 6
babaaba   clo: 4 chi: 7


"zbb"
0123
z     clo: 0 chi: 1
zb    clo: 1 chi: 2
zbb   clo: 2 chi: 3 // s[2] != s[1 - 1], but s[2] == s[2 - 1] return 1,3
*/

int main() {


  vector<int> t1 {7, 1, 5, 3, 6, 4};
  vector<int> t2 {1, 2, 3, 4, 5};
  vector<int> t3 {7, 6, 4, 3, 1};

  Solution s;

}
