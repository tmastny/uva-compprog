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
  string line;
  while(cin >> line) {
    if (line == "#") break;

    next_permutation(line.begin(), line.end());


    string first = line;
    sort(first.begin(), first.end());

    string output = line;
    if (line == first) {
      output = "No Successor";
    }

    cout << output << endl;
  }



}
