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

using namespace std;

// p(7) = 242 + 120 + 82 = 444
// p(0) = 73 + 49 + 58 = 180
// total               = 624
// --wrong--

int mod(int i, int bits) {
  return i & (bits - 1);
}

bool is_odd(int i) {
  return i % 2 == 1;
}

int main() {

  int dim;

  while (cin >> dim) {
    int corners = pow(2, dim);

    vector<int> weights;
    int weight;
    for (int c = 0; c < corners; c++) {
      cin >> weight;
      weights.push_back(weight);
    }

    vector<int> potencies;
    for (int i = 0; i < corners; i++) {

      int neighbor = i;
      int potency = 0;

      int sign = is_odd(i) ? -1 : 1;
      for (int j = 1; j <= corners / 2; j <<= 1) {
        neighbor = mod(neighbor + sign * j, corners);
        potency += weights[neighbor];
        // cout << "i: " << i << endl;
        // cout << "j: " << j << endl;
        // cout << "n: " << neighbor << endl;
        // cout << "p: " << potency << endl;
      }
      potencies.push_back(potency);
    }

    for (int i = 0; i < corners; i++) {
      cout << i << ": " << potencies[i] << endl;
    }

    int max_cube_sum = 0;
    for (int i = 0; i < corners; i++) {

      int max_neighbor_sum = 0;
      int neighbor = i;

      int sign = is_odd(i) ? -1 : 1;
      for (int j = 1; j <= corners / 2; j <<= 1) {
        neighbor = mod(neighbor + sign * j, corners);

        int neighbor_sum = potencies[i] + potencies[neighbor];
        if (neighbor_sum > max_neighbor_sum) {
          max_neighbor_sum = neighbor_sum;

          //cout << i << " " << neighbor << " " << max_neighbor_sum << endl;
        }
      }

      if (max_neighbor_sum > max_cube_sum) {
        max_cube_sum = max_neighbor_sum;
      }
    }

    cout << max_cube_sum << endl;
    // for (int i = 0; i < corners; i++) {
    //   for (int j = 0; j < corners; j++) {
    //     if (i == j) continue;
    //     if (potencies[i] + potencies[j] == 619)
    //       cout << i << " " << j << endl;
    //   }
    // }
  }

}
