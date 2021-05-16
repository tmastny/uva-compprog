#include <cstdio>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

void print_matrix(vector< vector<int> > &matrix) {
  for (int i = 0; i < matrix.size(); i++) {
    for (int j = 0; j < matrix[i].size(); j++) {
      cout << matrix[i][j] << " ";
    }
    cout << "\n";
  }
  cout << "\n";
}

void print_mines(vector< vector<int> > &matrix) {
  for (int i = 1; i < matrix.size() - 1; i++) {
    for (int j = 1; j < matrix[i].size() - 1; j++) {
      if (matrix[i][j] == 8) {
        cout << "*";
      } else {
        cout << matrix[i][j];
      }
    }
    cout << "\n";
  }
}

void left_right(vector< vector<int> > &matrix, int ncol, int nrow) {
  for (int i = 1; i <= nrow; i++) {
    for (int j = 1; j <= ncol; j++) {

      int mines = 0;
      if (matrix[i][j] == 8) {
        cout << '*';
        continue;
      }

      for (int k = i - 1; k <= i + 1; k++) {
        for (int l = j - 1; l <= j + 1; l++) {
          if (matrix[k][l] == 8) {
            mines += 1;
          }
        }
      }

      cout << mines;
    }
    cout << "\n";
  }
}

int main() {
  int nrows, ncols = 1;

  int field = 1;
  while (scanf("%d %d", &nrows, &ncols) != EOF) {
    if (nrows == 0 || ncols == 0) break;
    if (field > 1) printf("\n");
    printf("Field #%d:\n", field);


    vector<int> place_holder_row;
    for (int i = 0; i < ncols + 2; i++) {
      place_holder_row.push_back(0);
    }

    vector< vector<int> > matrix;
    matrix.push_back(place_holder_row);


    for (int i = 0; i < nrows; i++) {
      string mine_row;
      cin >> mine_row;

      vector<int> row;
      row.push_back(0);
      for (int i = 0; i < mine_row.length(); i++) {
        int indicator = 0;
        if (mine_row[i] == '*') {
          indicator = 8;
        }

        row.push_back(indicator);
      }
      row.push_back(0);

      matrix.push_back(row);
    }
    matrix.push_back(place_holder_row);


    left_right(matrix, ncols, nrows);

    // print_mines(matrix);
    field++;
  }
}
