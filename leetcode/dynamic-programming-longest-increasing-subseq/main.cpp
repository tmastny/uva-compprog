#include <vector>
#include <iostream>
#include <algorithm>
#include <set>

using namespace std;

struct RunNum {
  int val;
  int run_index;
};

bool operator<(const RunNum& lhs, const RunNum& rhs) {
    return lhs.val < rhs.val;
}

class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        auto nums_deduped = remove_successive_dups(nums);

        vector<vector<int>> nums_vi;
        for (int i = 0; i < nums.size(); i++) {
            nums_vi.push_back({nums[i], i});
        }

        stable_sort(nums_vi.begin(), nums_vi.end());

        set<RunNum> RunCounter {RunNum {nums_vi[0][1], 1}};
        for (int i = 1; i < nums_vi.size(); i++) {

        }


    }
};

vector<int> remove_successive_dups(vector<int>& nums) {
    vector<int> deduped = {nums[0]};
    for (int i = 1; i < nums.size(); i++) {
        if (nums[i] != nums[i - 1]) {
          deduped.push_back(nums[i]);
        }
    }

    return deduped;
}

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

}
