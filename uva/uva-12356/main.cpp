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

using namespace std;

//       1 2 3 4 5 6 7 8 9 10
// 2:5   1         6 7 8 9 10  1:6
// 6:7   1             8 9 10  1:8
// 1:8                   9 10  *:9

// could use doubly linked list or array
// array padding?
// I feel like you could do a set too
// uses binary search tree maintains order and
// as nice deletion

// actually in this case the binary search tree
// is degenerate: it's actually a doubly linked
// list, because the elements are ordered

int main() {
  int n_soldiers, reports;

  while(cin >> n_soldiers >> reports) {
    if (n_soldiers == 0) break;

    set<int> soldiers;
    for (int s = 0; s <= n_soldiers + 1; s++) {
      soldiers.insert(s);
    }

    int left, right;
    for (int r = 0; r < reports; r++) {
      cin >> left >> right;

      auto left_it = soldiers.find(left);
      auto right_it = soldiers.find(right);

      string surv_left = to_string(*next(left_it, -1));
      if (surv_left == "0") surv_left = "*";

      string surv_right = to_string(*next(right_it, 1));
      if (surv_right == to_string(n_soldiers + 1)) surv_right = "*";

      cout << surv_left << " " << surv_right << endl;

      soldiers.erase(left_it, next(right_it, 1));
    }


    cout << "-\n";

  }

}
