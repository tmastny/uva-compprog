#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    void swap(vector<int> & n, int i, int j) {
        int temp = n[i];
        n[i] = n[j];
        n[j] = temp;
    }

    void rotate(vector<int>& nums, int k) {
        int size = nums.size();

        if (size <= 1) return;

        int count = 1;
        for (int i = 0; count < size; i++) {

            int curr = i;
            int curr_value = nums[curr];
            while (true) {

                int next = (curr + k) % size;
                int next_value = nums[next];

                nums[next] = curr_value;

                curr = next;
                curr_value = next_value;

                count++;

                if (next == i) break;
            }
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
