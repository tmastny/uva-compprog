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
#include <bitset>
#include <list>

using namespace std;

int main() {

  string line;
  while (getline(cin, line)) {

    list<char> output;

    auto it = output.end();
    for (auto c : line) {

      if (c == '[') {
        it = output.begin();
        continue;

      } else if (c == ']') {
        it = output.end();
        continue;

      }

      output.insert(it, c);
    }

    for (auto c : output)
      cout << c;

    cout << endl;
  }

}
