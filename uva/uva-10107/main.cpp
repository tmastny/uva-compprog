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

int main() {
  int x, median;
  vector<int> list;
  while (cin >> x) {
    list.push_back(x);

    sort(list.begin(), list.end());

    int size = list.size();
    if (size % 2 == 0) {
      cout << (list[size / 2 - 1] + list[size/2]) / 2 << endl;
    } else {
      cout << list[size/2] << endl;
    }
  }




}
