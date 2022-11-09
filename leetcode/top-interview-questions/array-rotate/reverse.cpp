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

    void reverse(vector<int> & n, int start, int end) {

        while (start < end) {
            swap(n, start, end);
            start++;
            end--;
        }

    }

    void rotate(vector<int>& nums, int k) {

        int size = nums.size();
        if (size <= 1) return;

        k = k % size;

        reverse(nums, 0, size - 1);
        reverse(nums, 0, (k - 1) % size);
        reverse(nums, k % size, size - 1);
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
