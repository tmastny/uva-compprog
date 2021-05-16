#include <cstdio>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <set>

using namespace std;

string digit_outer_column(string c, bool top, bool left) {
  if (c == "8" || c == "0") {
    return "|";
  }

  if (c == "1" || c == "3" || c == "7") {
    if (!left) return "|";
    return " ";
  }

  if (c == "4" || c == "9") {
    if (left && !top) {
      return " ";
    }
    return "|";
  }

  if (c == "2") {
    if (top && left) return " ";
    if (!top && !left) return " ";
    return "|";
  }

  if (c == "5") {
    if (top && left) return "|";
    if (!top && !left) return "|";
    return " ";
  }

  if (c == "6") {
    if (top && !left) return " ";
    return "|";
  }


  return c;

}

string digit_inner_row(string c, int row, int rows) {

  if (c == "1") {
    return " ";
  }

  if (c == "4") {
    if (row % rows == 0) {
      return " ";
    }
    return "-";

  }

  if (c == "7") {
    if (row == 0) {
      return "-";
    }
    return " ";
  }

  if (c == "0") {
    if (row % rows != 0)
      return " ";

    return "-";
  }

  return "-";
}

void print_digit(int s, string c) {

  int cols = s + 2 - 1;
  int rows = 2 * s + 3 - 1;

  for (int r = 0; r <= rows; r++) {
    bool top = r < rows / 2;

    string outerr = digit_outer_column(c, top, false);
    string outerl = digit_outer_column(c, top, true);
    string inner = " ";

    if (r % (rows / 2) == 0) {
      outerr = outerl = " ";
      inner = digit_inner_row(c, r, rows);
    }

    cout << outerl;
    for (int c = 1; c < cols; c++) {
      cout << inner;
    }

    cout << outerr << "\n";
  }
}

int main() {
  int spaces;
  string number;

  while (cin >> spaces, cin >> number, spaces != 0) {
    print_digit(spaces, number);
  }
}
