#include <vector>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <iterator>

using namespace std;

vector<int> remove_successive_dups(vector<int>& nums) {
    vector<int> deduped = {nums[0]};
    for (int i = 1; i < nums.size(); i++) {
        if (nums[i] != nums[i - 1]) {
          deduped.push_back(nums[i]);
        }
    }

    return deduped;
}

class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        auto nums_deduped = remove_successive_dups(nums);

        map<int, int> RunCounter {{nums_deduped[0], 1}};
        int prev_run_length = 1;
        for (int i = 1; i < nums_deduped.size(); i++) {
            int n = nums_deduped[i];

            auto it = RunCounter.lower_bound(n);

            int run_length = 1;
            if (it != RunCounter.begin()) {
                run_length = prev(it)->second + 1;
            }

            if (n > nums_deduped[i - 1]) {
                run_length = max(run_length, prev_run_length + 1);
            }

            RunCounter[n] = run_length;
            prev_run_length = run_length;
        }

        int max_run_length = 0;
        for (auto run : RunCounter) {
            if (run.second > max_run_length) {
              max_run_length = run.second;
            }
        }

        return max_run_length;
    }
};

int main() {
    vector<tuple<vector<int>, int>> cases = {
        {{10, 11, 12, 13, 14, 1, 2, 3}, 5},
        {{1, 2, 10, 3, 4}, 4},
        {{0, 10, 11, 12, 13, 1, 2, 3, 4, 5}, 6},
        {{10, 9, 2, 5, 3, 7, 101, 18}, 4},
        {{0, 9, 4, 10, 3, 15, 5, 18, 1, 20}, 6},
        {{0, 1, 0, 3, 2, 3}, 4},
        {{7, 7, 7, 7, 7, 7, 7}, 1},
        {{7, 6, 7, 8}, 3},   // have to be careful about how to handle duplicates
        {{0, 7, 6, 1, 5, 2, 4, 3}, 4},
        {{7, 6, 5, 4, 3, 2, 1, 0}, 1},
        {{41, 20, 30, 21, 22, 23, 24, 10}, 5},
        {{7, 1, 5, 2, 3, 4, 6, 0}, 5},
        {{100, 99, 98, 97, 96, 21, 22, 23, 0, 1}, 3},
        {{100, 99, 98, 97, 96, 21, 110, 22, 109, 23, 101, 0, 1}, 4},
        {{10, 23, 41, 3, 61}, 4}
    };

    Solution s;

    for (auto&& test : cases) {
        cout << s.lengthOfLIS(get<0>(test)) << " " << get<1>(test) << endl;
        //cout << "*******" << endl;
    }

}
