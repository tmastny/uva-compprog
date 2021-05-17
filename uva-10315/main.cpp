#include <cstdio>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <set>
#include <map>

using namespace std;


int value_to_int(const char & value) {
  string values = "23456789TJQKA";

  for (int i = 0; i < values.length(); i++)
    if (values[i] == value)
      return i;

  return -1;
}

int main() {
  string line;
  string card;

  while (getline(cin, line)) {
    stringstream ss(line);

    vector<string> black;
    for (int i = 0; i < 5; i++) {
      ss >> card;
      black.push_back(card);
    }

    vector<string> white;
    for (int i = 0; i < 5; i++) {
      ss >> card;
      white.push_back(card);
    }

    map<int, int> values;
    map<string, int> suits;
    for (auto c : black) {
      int value = value_to_int(c[0]);
      string suit = string{c[1]};

      if (values.find(value) == values.end())
        values[value] = 0;
      values[value] += 1;

      if (suits.find(suit) == suits.end())
        suits[suit] = 0;
      suits[suit] += 1;
    }

    cout << "black: \n";
    for (auto const & x : values) cout << x.first << "-" << x.second << endl;







    // cout << "black: ";
    // for (auto i : black) cout << i << " ";

    // cout << "| white: ";
    // for (auto i : white) cout << i << " ";
    // cout << endl;
  }
}
