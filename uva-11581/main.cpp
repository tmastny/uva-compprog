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

vector<int> line_to_row(string line) {
  vector<int> row;

  row.push_back(0);
  for (auto c: line) {
    row.push_back(stoi(string (1 , c)));
  }
  row.push_back(0);

  return row;
}

void pad(vector<vector<int>> & grid) {
  vector<int> row;
  for (int i = 0; i < 5; i++) {
    row.push_back(0);
  }
  grid.push_back(row);
}

vector<vector<int>> grid_fun(vector<vector<int>> & grid) {

  vector<vector<int>> trans_grid;
  for (int j = 0; j < 5; j++) {
    pad(trans_grid);
  }


  for (int r = 1; r <= 3; r++) {
    for (int c = 1; c <= 3; c++) {

      int sum = 0;
      for (int i = -1; i <= 1; i++) {
        for (int j = -1; j <= 1; j++) {
          if (abs(i) == 1 && abs(j) == 1) continue;
          if (i == 0 && j == 0) continue;
          sum ^= grid[r + i][c + j];
        }
      }

      trans_grid[r][c] = sum;
    }
  }
  return trans_grid;
}

void print(vector<vector<int>> & grid) {
  for (int r = 1; r <= 3; r++) {
    for (int c = 1; c <= 3; c++) {
      cout << grid[r][c];
    }
    cout << endl;
  }
  cout << endl;
}

bool equal(vector<vector<int>> & g1, vector<vector<int>> & g2) {

  bool is_equal = true;

  for (int r = 0; r < 5; r++) {
    for (int c = 0; c < 5; c++) {
      is_equal &= g1[r][c] == g2[r][c];
    }
  }

  return is_equal;
}

int main() {
  int cases;
  cin >> cases;

  while(cases--) {
    string line;
    getline(cin, line);

    vector<vector<int>> grid;
    pad(grid);
    for (int i = 0; i < 3; i++) {
      cin >> line;
      grid.push_back(line_to_row(line));
    }
    pad(grid);


    vector<vector<int>> zero_grid;
    for (int i = 0; i < 5; i++) {
      pad(zero_grid);
    }

    int i = 0;
    while(!equal(grid, zero_grid)) {
      grid = grid_fun(grid);
      i++;
    }

    cout << i - 1 << endl;
  }

}
