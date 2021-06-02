#include <vector>
#include <iostream>
#include <map>

using namespace std;

class Solution {
public:

    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        sort(nums1.begin(), nums1.end());
        sort(nums2.begin(), nums2.end());


        auto index_in_bounds = [&nums1, &nums2](int & i1, int & i2) {
            return i1 < nums1.size() && i2 < nums2.size();
        };

        int i1 = 0;
        int i2 = 0;

        vector<int> intersect;

        while (index_in_bounds(i1, i2)) {

            while (index_in_bounds(i1, i2) && nums1[i1] <= nums2[i2]) {

                if (nums1[i1] == nums2[i2]) {
                    intersect.push_back(nums1[i1]);
                    i1++;
                    i2++;
                    break;
                }

                i1++;
            }

            while (index_in_bounds(i1, i2) && nums1[i1] > nums2[i2]) {
                i2++;
            }
        }

        return intersect;
    }
};

int main() {


    vector<int> t1 {7, 1, 5, 3, 6, 4};
    vector<int> t2 {1, 2, 3, 4, 5};
    vector<int> t3 {7, 6, 4, 3, 1};

    Solution s;

    for (auto i : s.intersect(t1, t2)) {
        cout << i << endl;
    }

    cout << "---" << endl;
    int i = 1;
    int& p = i;

    p++;

    cout << i << endl;

}
