#include <vector>
#include <map>
#include <iostream>

using namespace std;

class Solution {
public:
    int brute_force(vector<int>& nums) {

        int max_sum = INT_MIN;

        for (int i = 0; i <= nums.size() - 1; i++) {
            for (int j = i; j <= nums.size() - 1; j++) {

                int sum = 0;
                for (int k = i; k <= j; k++) {
                    sum += nums[k];
                }

                if (sum > max_sum) {
                    max_sum = sum;
                }
            }
        }

        return max_sum;

    }

    int linear(vector<int>& nums) {
        int maxsum = nums[0];
        int cumsum = nums[0];

        for (int i = 1; i < nums.size(); i++) {
            if (cumsum < 0) cumsum = 0;

            cumsum += nums[i];
            if (cumsum > maxsum) {
                maxsum = cumsum;
            }
        }

        return maxsum;
    }

    int maxSubArray(vector<int>& nums) {

        //    1 <= nums.length <= 3 * 104
        // -105 <= nums[i]     <= 105

        for (int i = 0; i < 100; i++) {

            vector<int> test_array;
            int length = rand() % 100 + 5;
            for (int j = 0; j < length; j++) {
                test_array.push_back(rand() % 1001 + -500);
            }

            if (linear(test_array) != brute_force(test_array)) {
                cout << "error: " << linear(test_array) << " " << brute_force(test_array) << endl;

                for (auto t : test_array) {
                    cout << t << " ";
                }

                cout << endl;

                break;
            }
        }


        return linear(nums);
    }
};
