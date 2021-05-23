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

// solution: https://www.davidudelson.com/blog/2015/06/23/uva-10920-spiral-tap/
// I noticed the growing squares,
// but did not connect it to the pattern of 1, 2, 3, 4, 5 I noticed
// when you simulate walking the spiral.

// Likewise, I didn't consider the scale of the input would be
// 100000^2


// 3 2 9
// 4 1 8
// 5 6 7

bool is_even(int i) {
  return i % 2 == 0;
}

int main() {
  int size, pos;

  while(cin >> size >> pos) {
    if (size == 0 && pos == 0) break;

    int row = size / 2;
    int col = size / 2;
    int p = 1;
    for (int i = 1; i <= size; i++) {
      if (p == pos) break;


      int v = 1;
      int h = -1;
      if (is_even(i)) {
        v = -1; h = 1;
      }


      for (int j = 0; j < i; j++) {
        row += v;
        p++;

        // cout << row + 1 << " " << col + 1 << " " << p << endl;
        if (p == pos) break;
      }

      if (p == pos) break;

      for (int j = 0; j < i; j++) {
        col += h;
        p++;

        // cout << row + 1 << " " << col + 1 << " " << p << endl;
        if (p == pos) break;
      }
    }

    cout << "Line = " << row + 1 << ", column = " << col + 1 << ".\n";

  }
}
