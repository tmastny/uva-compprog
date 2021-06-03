#include <vector>
#include <iostream>
#include <map>

using namespace std;

// Complexity: O(n_1 + n_2).

// Both `map` and `sorted` are O(n), but the sorted method
// should be significantly faster. On each step of `map`,
// the solution must pay the constant `hash` cost (or O(logn)
// lookup. Moreover, it does not require extra memory beyond
// the output array.

// If `nums1.size()` is small compared to `nums2.size()`,
// sorted still should be faster. Is `nums1` is much smaller,
// and `nums2` is sorted, you could do binary search in `nums2`
// for each element of `nums1` for a complexity of O(n_1 log n_2).
// This is better than O(n_1 + n_2).


// `nums2` on disk:
// The first solution won't work. In the degenerate case,
// where each value of `nums2` is unique, the entire vector
// must be stored in memory (or written to an external database).

// If `nums2` could be sorted on the disk, then the sorted solution
// works with only minor modification. Each element of `nums2` is
// only pulled one at a time, and immediately written to the output
// array if applicable. It does not require storage (beyond the
// output vector, which may be external).


// cleaner solution: https://medium.com/@punitkmr/intersection-of-two-arrays-ii-ffb26f04dfd1
// while (i < nums1.length && j < nums2.length) {
//     if (nums1[i] == nums2[j]) {
//         result.add(nums1[i]);
//         i++;
//         j++;
//     } else if (nums1[i] < nums2[j]){
//         i++;
//     } else {
//         j++;
//     }
// }



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
