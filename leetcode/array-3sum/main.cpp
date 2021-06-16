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

public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        return threeSumOn2(nums);
    }
};

int main() {


  vector<int> t1 {7, 1, 5, 3, 6, 4};
}
