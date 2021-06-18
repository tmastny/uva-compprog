#include <cstdio>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <tuple>
#include <numeric>
#include <iterator>
#include <cmath>

using namespace std;



class Solution {
  public:
    int removeDuplicates(vector<int>& nums) {
      if (nums.size() <= 1) return nums.size();

      int k = 0;
      for (int i = 1; i < nums.size(); i++) {
        if (nums[k] != nums[i]) {
          nums[++k] = nums[i];
        }
      }

      return k + 1;
    }

    void swap(vector<int>& nums, int i, int j) {
      int temp = nums[i];
      nums[i] = nums[j];
      nums[j] = temp;
    }
};

int main() {


}
