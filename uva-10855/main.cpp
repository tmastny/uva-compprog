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

void print_sq(vector<vector<char>> & sq) {
  for (auto r : sq) {
    for (auto c : r) {
      cout << c << " ";
    }
    cout << endl;
  }
}

vector<vector<char>> make_square(int size) {

  vector<vector<char>> sq;
  for (int i = 0; i < size; i++) {
    string line;
    cin >> line;

    sq.push_back(vector<char> (line.begin(), line.end()));
  }

  return sq;
}


void rotate_sq(vector<vector<char>> sq) {
  return;
}


int nested_sqs(vector<vector<char>> & big, vector<vector<char>> & lil) {
  int sqs = 0;

  for (int big_col = 0; big_col <= big.size() - lil.size(); big_col++) {
    for (int big_row = 0; big_row <= big.size() - lil.size(); big_row++) {

      bool is_match = true;

      for (int lil_row = 0; lil_row < lil.size(); lil_row++) {
        for (int lil_col = 0; lil_col < lil.size(); lil_col++) {

          // cout << "row: " << lil_row << " " << lil_col << endl;

          // cout << lil[lil_row][lil_col] << endl;
          // cout << big[big_row][lil_col] << endl;

          // cout << big[big_row + lil_row][big_col + lil_col] << " ";

          is_match &= lil[lil_row][lil_col] == big[big_row + lil_row][big_col + lil_col];

        }

        // cout << endl;
      }
      // cout << endl;

      if (is_match) sqs++;
    }
  }

  return sqs;
}

vector<vector<char>> rotate(vector<vector<char>> & sq) {

  vector<vector<char>> temp_sq;
  vector<char> temp_row;
  for (int c = 0; c < sq.size(); c++) {

    vector<char> temp_row;
    for (int r = sq.size() - 1; r >= 0; r--) {

      temp_row.push_back(sq[r][c]);
    }
    temp_sq.push_back(temp_row);
  }

  return temp_sq;
}

// Clockwise rotation
// __  __  __  __
// 0   90  180 270

int main() {
  int big_sq_size, lil_sq_size;

  while(cin >> big_sq_size >> lil_sq_size) {
    if (big_sq_size == 0) break;

    auto big_sq = make_square(big_sq_size);
    auto lil_sq = make_square(lil_sq_size);


    for (int i = 0; i < 4; i++) {
      cout << nested_sqs(big_sq, lil_sq) << " ";

      lil_sq = rotate(lil_sq);
    }
    cout << endl;


    // int sqs = nested_sqs(big_sq, lil_sq);
    // cout << "nested sqs: " << sqs << endl;
  }

}
