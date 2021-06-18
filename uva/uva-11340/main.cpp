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

  for (int n = 0; n < tests; n++) {

    int characters;
    cin >> characters;

    map<char, int> character_pay;
    for (int k = 0; k < characters; k++) {
      char c;
      cin >> c;

      int p;
      cin >> p;
      character_pay[c] = p;
    }

    int lines;
    cin >> lines;

    int pay = 0;
    string line;
    for (int l = 0; l < lines; l++) {

      getline(cin, line);

      for (auto c: line) {

        if (character_pay.find(c) != character_pay.end())
          pay += character_pay[c];
      }
    }


    printf("%.2lf$\n", pay / 100.0);



  }


}
