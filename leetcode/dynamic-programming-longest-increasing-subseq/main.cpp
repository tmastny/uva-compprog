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
        if (nums.size() == 1) return 1;

        auto nums_deduped = remove_successive_dups(nums);

        map<int, int> RunLength {{nums_deduped[0], 1}};

		int top_of_longest_run = nums_deduped[0];

		for (int i = 1; i < nums_deduped.size(); i++) {
            int n = nums_deduped[i];

            if (n > top_of_longest_run) {
				RunLength[n] = RunLength[top_of_longest_run] + 1;
				top_of_longest_run = n;

			} else {
				auto it = RunLength.lower_bound(n);
				int run_length = 1;
				if (it != RunLength.begin()) {
					run_length = prev(it)->second + 1;
				}

				RunLength[n] = run_length;
				if (run_length > RunLength[top_of_longest_run]) {
					top_of_longest_run = n;
				}
			}
			cout << n << " " << RunLength[n] << endl;
        }

        int max_run_length = 0;
        for (auto run : RunLength) {
            if (run.second > max_run_length) {
              max_run_length = run.second;
            }
        }

        return max_run_length;
    }
};

int main() {
    vector<tuple<vector<int>, int>> cases = {
        // {{10, 11, 12, 13, 14, 1, 2, 3}, 5},
        // {{1, 2, 10, 3, 4}, 4},
        // {{0, 10, 11, 12, 13, 1, 2, 3, 4, 5}, 6},
        // {{10, 9, 2, 5, 3, 7, 101, 18}, 4},
        // {{0, 9, 4, 10, 3, 15, 5, 18, 1, 20}, 6},
        // {{0, 1, 0, 3, 2, 3}, 4},
        // {{7, 7, 7, 7, 7, 7, 7}, 1},



		// the problem is 11 matches 10, because -5 and 10 are tied.
		// Then 12 matches 11 for a run length of 3.
		// Ties are currently broken in favor of the lower bound,
		// because the max run length is only updated on >, not >=
		// So it this case it checks against 15 as `top_of_longest_run`
		// rather than -5. But should ties always break for the most recent run?
		    {{10, 15, 20, -10, -5, 11, 12}, 4},
		// rl: 1   2   3    1   2   3   4

		// this example proves it's not just the most recent sequence.
		    {{10, 15, 20, -10, -5, -50, 11, 12}, 4},

		// 4 values less than 11
		//	10, -10, -5, -50
		//            ^------> -5 is the value with the longest run
		// Problem:
		// 	1. requires finding all previous values less than 11.
		//	   Not a problem with binary search tree
		//
		//  2. of those, which has the max run length. Obvious method is O(n)
		//     which is too slow. Unclear how to use a heap here.

		// Is it possible to use the number of elements less than the 11,
		// like used in an order tree?



        // // which subsequence should the last element continue?
        // // the latest element needs to continue whichever is the longest
        // // forms the longest subseqence.
        // //              should match to 8
        //             {{9, 7, 8, 6, 10}, 3},
        //         {{10, 9, 7, 8, 6, 11}, 3},
        // {{1, 2, 3, 4, 9, 7, 8, 6, 10}, 7},

        // //               should match to 9
        //       {{7, 8, 9, 7, 8, 6, 10}, 4},
        //   {{10, 7, 8, 9, 7, 8, 6, 11}, 4},

        // // 80 or 60 are valid continuations
        //     {{80, 60, 100}, 2},
        //     {{80, 60, 100, 61, 62}, 3},
        //     {{80, 60, 100, 81, 82}, 3},

        // {{9, 7, 8, 6, 10, 7, 8, 9}, 4}
    };

    Solution s;

    for (auto&& test : cases) {
        int calc = s.lengthOfLIS(get<0>(test));
		int ans = get<1>(test);

		if (calc != ans) {
			cout << "Wrong Answer: ";
		}

		cout << calc << " " << ans << endl;
        cout << "*******" << endl;
    }

}

		// {{9, 7, 8, 6, 10}, 3},

		//    counter  run
		// 9   1       1
		// 7   1       1
		// 8   2       2 @ 8
		// 6   1       2 @ 8
		// 10          3 @ 10
