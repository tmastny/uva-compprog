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

int mod(int i, int bits) {
  return i & (bits - 1);
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
      for (int j = 1; j <= corners / 2; j <<= 1) {
        neighbor = mod(neighbor + j, corners);
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

    for (int i = 0; i < corners; i++) {
      for (int j = 0; j < corners; j++) {
        if (i == j) continue;
        if (potencies[i] + potencies[j] == 619)
          cout << i << " " << j << endl;
      }
    }

    break;
  }

}
