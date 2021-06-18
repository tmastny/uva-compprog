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
// - the upper right corners are the squares of the size of the square

// 3 2 9
// 4 1 8
// 5 6 7

int corner(int ending, int starting) {
  return ending - (ending - starting) / 2;
}

int main() {
  int size, pos;

  while(cin >> size >> pos) {
    if (size == 0 && pos == 0) break;


    int inner_ring = 1;
    int outer_ring = 1;
    int ring_num = 0;

    while (pos > outer_ring * outer_ring) {
      ring_num++;
      inner_ring = outer_ring;
      outer_ring = outer_ring + 2;
    }

    // (i - 1)^2 < pos <= i^2
    // ex: 9 < pos <= 25

    // if I need to save time, I can do a sort of
    // binary search to find the edge, so instead of searching
    // 0(n^2) it would take O(sqrt(n)), or one side of the square.

    // although searching all the sides is just 4sqrt(n) == O(sqrt(n))

    // example:



    int lower_left = corner(outer_ring * outer_ring, inner_ring * inner_ring);
    int upper_left = corner(lower_left, inner_ring * inner_ring);
    int lower_right = corner(outer_ring * outer_ring, lower_left);
    int upper_right = outer_ring * outer_ring;


    int lower_corner_index = (size + 1) / 2 - ring_num;
    int upper_corner_index = (size + 1) / 2 + ring_num;


    int row, col;
    if (pos <= upper_left) {

      row = upper_corner_index;
      col = lower_corner_index + (upper_left - pos);

    } else if (pos <= lower_left) {

      row = lower_corner_index + (lower_left - pos);
      col = lower_corner_index;

    } else if (pos <= lower_right) {

      row = lower_corner_index;
      col = upper_corner_index - (lower_right - pos);

    } else {

      row =  upper_corner_index - (upper_right - pos);
      col = upper_corner_index;

    }

    cout << "Line = " << row << ", column = " << col << ".\n";
  }
}
