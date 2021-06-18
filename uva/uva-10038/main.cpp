#include <cstdio>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <set>

using namespace std;

int main() {
  int n;
  string line;

  while (cin >> n) {

    vector<int> seq;
    for (int i = 0; i < n; i++) {
      int j;
      cin >> j;
      seq.push_back(j);
    }

    set<int> diffs;
    for (int i = 0; i < n - 1; i++) {
      diffs.insert(abs(seq[i] - seq[i + 1]));
    }

    string output = "Jolly";
    for (int i = 1; i <= n - 1; i++) {
      if (diffs.find(i) == diffs.end()) {
        output = "Not jolly";
        break;
      }
    }

    cout << output << endl;
  }
}
