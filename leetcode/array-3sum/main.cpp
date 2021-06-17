#include <vector>
#include <set>
#include <iostream>

using namespace std;

class Solution {
private:
    int sum(vector<int>& pair) {
        int sum = 0;
        for (auto p : pair) {
            sum += p;
        }

        return sum;
    }

    vector<int> add_sort(vector<int> n, int j) {
        n.push_back(j);
        sort(n.begin(), n.end());

        return n;
    }

    vector<int> pair(int i, int j) {
        vector<int> pair;
        pair.push_back(i);
        pair.push_back(j);

        sort(pair.begin(), pair.end());

        return pair;
    }

    vector<vector<int>> threeSumOn2(vector<int>& nums) {
        if (nums.size() < 3) return vector<vector<int>>();

        set<vector<int>> threes;
        set<vector<int>> pairs;
        for (int i = 1; i < nums.size(); i++) {

            for (auto pair : pairs) {
                if (nums[i] + sum(pair) == 0) {
                    threes.insert(add_sort(pair, nums[i]));
                }
            }

            for (int j = i - 1; j >= 0; j--) {
                pairs.insert(pair(nums[i], nums[j]));
            }
        }


        vector<vector<int>> triplets;
        for (auto t : threes) {
            triplets.push_back(t);
        }

        return triplets;
    }
    vector<int> make_triplet(int i, int j, int k) {
        vector<int> triplet;
        triplet.push_back(i);
        triplet.push_back(j);
        triplet.push_back(k);

        sort(triplet.begin(), triplet.end());

        return triplet;
    }

    // This solution was almost good enough, time exceeded on the second
    // to last problem. Something to do with zeroes...
    vector<vector<int>> threeSumOnlogn(vector<int>& nums) {
        set<vector<int>> threes;

        sort(nums.begin(), nums.end());

        int neg = 0;
        while (neg < nums.size() && nums[neg] <= 0) {
            // cout << "neg: " << neg << ", " << nums[neg] << endl;

            int pos = nums.size() - 1;
            while (pos > neg && nums[pos] >= 0) {
                int two_sum = -1 * (nums[neg] + nums[pos]);

                // cout << "pos: " << pos << ", " << nums[pos] << " twosum: " << two_sum << endl;

                if (two_sum > nums[pos]) break;

                auto begin = next(nums.begin(), neg + 1);
                auto end = next(nums.begin(), pos);

                if (binary_search(begin, end, two_sum)) {
                    cout << "found match" << endl;
                    threes.insert(make_triplet(nums[neg], nums[pos], two_sum));
                }

                pos--;
            }
            neg++;
        }


        vector<vector<int>> triplets;
        for (auto t : threes) {
            triplets.push_back(t);
        }

        return triplets;
    }
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        return threeSumOn2(nums);
    }


};

int main() {


  vector<int> t1 {7, 1, 5, 3, 6, 4};
}
// [-1,0,1,2,-1,-4]
// [0,1]
// [-1,-1,4,5,0,2,3,4,-1,-2,-3,-4]
// [0,0,0,0]
