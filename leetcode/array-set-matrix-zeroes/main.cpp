#include <vector>
#include <set>
#include <iostream>

using namespace std;


class Solution {
private:
    void set_row_col_to_code(vector<vector<int>>& matrix, int row, int col, int code) {
        for (int c = 0; c < matrix[0].size(); c++) {
            if (matrix[row][c] != 0) {
                matrix[row][c] = code;
            }
        }

        for (int r = 0; r < matrix.size(); r++) {
            if (matrix[r][col] != 0) {
                matrix[r][col] = code;
            }
        }
    }

    void code_matrix(vector<vector<int>>& matrix, int code) {
        for (auto& row : matrix) {
            for (auto& entry : row) {
                if (entry != 0 &&
                    entry < INT_MAX - abs(code) &&
                    INT_MIN + abs(code) < entry &&
                    entry + abs(code)
                )
                {
                    entry += code;
                }
            }
        }
    }

    int mcode = 256;

public:
    void setZeroes(vector<vector<int>>& matrix) {

        code_matrix(matrix, mcode);

        for (int r = 0; r < matrix.size(); r++) {
            for (int c = 0; c < matrix[0].size(); c++) {
                if (matrix[r][c] == 0) {
                    set_row_col_to_code(matrix, r, c, mcode);
                }
            }
        }

        code_matrix(matrix, -1 * mcode);
    }
};
int main() {


  vector<int> t1 {7, 1, 5, 3, 6, 4};
}
// [-1,0,1,2,-1,-4]
// [0,1]
// [-1,-1,4,5,0,2,3,4,-1,-2,-3,-4]
// [0,0,0,0]
