#include <cstdio>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <tuple>

using namespace std;

map<string, map<string, int>> hands_rank {
  {"straight flush", {{"rank", 9}, {"value", 0}}},
  {"four", {{"rank", 8}, {"value", 0}}},
  {"full house", {{"rank", 7}, {"value", 0}}},
  {"flush", {{"rank", 6}, {"value", 0}}},
  {"straight", {{"rank", 5}, {"value", 0}}},
  {"three", {{"rank", 4}, {"value", 0}}},
  {"two-pairs", {{"rank", 3}, {"value", 0}}},
  {"pair", {{"rank", 2}, {"value", 0}}},
  {"high", {{"rank", 1}, {"value", 0}}},
};

int value_to_int(const char & value) {
  string values = "23456789TJQKA";

  for (int i = 0; i < values.length(); i++)
    if (values[i] == value)
      return i + 1;

  return -1;
}

vector<int> is_straight(map<int, int> values) {
  vector<int> values_in_order;
  for (auto x : values) {
    values_in_order.push_back(x.first);
  }
  sort(values_in_order.begin(), values_in_order.end());

  for (int i = 0; i < values_in_order.size() - 1; i++) {
    if (values_in_order[i + 1] - values_in_order[i] != 1) {
      return false;
    }
  }
  return vector<int> {hands["straight"], values_in_order[values_in_order.size() - 1]};
}

bool is_flush(map<int, int> suits) {
  return vector<int> {hands["flush"], values_in_order[values_in_order.size() - 1]};
}


tuple<string, int>  combo(map<int, int> values) {

  vector<int> hand;
  vector<vector<int>> hands;

  map<string, int> hands;

  for (auto x : values) {

    if (x.second == 4) {
      hands_rank["four"]["value"] = x.first;

    } else if (x.second == 3) {
      hands_rank["three"]["value"] = x.first;

    } else if (x.second == 2) {

      if (hands_rank["pair"]["value"] != 0) {
        hands_rank["two-pair"]["value"] = max(hands_rank["pair"]["value"], x.first);
      }
      hands_rank["pair"]["value"] = x.first;

    } else {

      hands_rank["high"]["value"] = max(hands_rank["high"]["value"], x.first);
    }
  }






  return make_tuple(max_value, max_freq);
}




tuple<int, int> best_value(map<int, int> values) {
  int max_freq = 1;
  int max_value = 1;
  for (auto x : values) {
    if (x.second > max_freq) {
       max_freq = x.second;
       max_value = x.first;
    }
  }

  if


  return make_tuple(max_value, max_freq);
}



string high_card(map<int, int> black, map<int, int> white) {

}

int main() {
  string line;
  string card;

  while (getline(cin, line)) {b v\
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
