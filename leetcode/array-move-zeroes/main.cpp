#include <vector>
#include <iostream>

using namespace std;

// I applied the lowest index tracker from another problem.

// Ah this was almost the optimal solution,
// but we can do it in one pass. Also, interesting
// scopoing trick in a for loop. Does that work in Java?

// void moveZeroes(vector<int>& nums) {
//     for (int lastNonZeroFoundAt = 0, cur = 0; cur < nums.size(); cur++) {
//         if (nums[cur] != 0) {
//             swap(nums[lastNonZeroFoundAt++], nums[cur]);
//         }
//     }
// }

class Solution {
public:
    void swap(vector<int>& n, int i, int j) {
        int temp = n[i];
        n[i] = n[j];
        n[j] = temp;
    }

    void moveZeroes(vector<int>& nums) {
        int lo = -1;

        for (int i = 0; i < nums.size(); i++) {

            if (lo == -1 && nums[i] != 0) {
                lo = i;
            }
        }

        for (int i = 0; i < nums.size(); i++) {

            if (nums[i] == 0) {
                continue;
            }

            if (i == lo) {
                swap(nums, i, 0);
                lo = 0;
                continue;
            }

            swap(nums, i, lo + 1);
            lo++;
        }
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
