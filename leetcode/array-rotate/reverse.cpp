#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
      return prices[0];
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
