#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        set<char> next_substr;
        set<char> best_substr;
        best_substr.insert(s[0]);

        int lo = 0;
        int hi = 1;
        int index_after_dup = 0;
        bool has_seen_dup = false;

        for (int i = 1; i < s.size(); i++) {
            if (!has_seen_dup) {
                if (best_substr.find(s[i]) == best_substr.end()) {
                    hi++;
                    best_substr.insert(s[i]);

                } else {
                    has_seen_dup = true;
                    while (s[index_after_dup] != s[i]) index_after_dup += 1;
			        index_after_dup += 1;

                    for (int j = index_after_dup; j <= i; j++) {
                        next_substr.insert(s[j]);
                    }
                }


            } else {
                if (next_substr.find(s[i]) == next_substr.end()) {
                    cout << s[i] << endl;
                    next_substr.insert(s[i]);

                    if (next_substr.size() > best_substr.size()) {
                        lo = index_after_dup;
                        hi = i + 1;
                        best_substr = next_substr;
                        next_substr.clear();
                    }
                } else {
                    index_after_dup = i;
                }
            }
        }

        for (auto b : next_substr) cout << b;
        cout << endl;

        for (auto b : best_substr) cout << b;
        cout << endl;
        return best_substr.size();
    }
};

int main() {


  vector<int> t1 {7, 1, 5, 3, 6, 4};
  vector<int> t2 {1, 2, 3, 4, 5};
  vector<int> t3 {7, 6, 4, 3, 1};

  Solution s;

  cout << s.maxProfit(t1) << endl;
  cout << s.maxProfit(t2) << endl;
  cout << s.maxProfit(t3) << endl;

}
