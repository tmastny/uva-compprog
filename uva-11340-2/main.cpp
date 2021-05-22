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

using namespace std;

int main() {
  int tests;
  cin >> tests;

  int character_pay[256] = {0};

  for (int n = 0; n < tests; n++) {

    int characters;
    cin >> characters;

    for (int k = 0; k < characters; k++) {
      char c;
      cin >> c;

      int p;
      cin >> p;
      character_pay[(int)c] = p;
    }

    int lines;
    cin >> lines;

    int pay = 0;
    string line;
    for (int l = 0; l < lines; l++) {

      getline(cin, line);

      for (auto c: line) {
        pay += character_pay[c];
      }
    }

    printf("%.2lf$\n", pay / 100.0);
  }
}
