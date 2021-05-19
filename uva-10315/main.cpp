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

int value_to_int(const char & value) {
  string values = "23456789TJQKA";

  for (int i = 0; i < values.length(); i++)
    if (values[i] == value)
      return i + 1;

  return -1;
}

double straight_rank(map<int, int> & values) {
  vector<int> values_in_order;
  for (auto x : values) {
    values_in_order.push_back(x.first);
  }
  sort(values_in_order.begin(), values_in_order.end());

  for (int i = 0; i < values_in_order.size() - 1; i++) {
    if (abs(values_in_order[i + 1] - values_in_order[i]) > 1) {
      return 10.0;
    }
  }
  return 2.75;
}

double flush_rank(map<string, int> & suits) {
  return suits.size() == 1 ? 2.5 : 10.0;
}

double hand_rank(tuple<map<int, int>, map<string, int>> & hand) {
  auto values = get<0>(hand);
  auto suits = get<1>(hand);

  cout << values.size() << " " << straight_rank(values) << " " << flush_rank(suits) << endl;

  return 6 - min({1.0 * values.size(), straight_rank(values), flush_rank(suits)});
}

tuple<double, vector<pair<int, int>>> hand_comparator(tuple<map<int, int>, map<string, int>> & hand) {

  vector<pair<int, int>> count_value;
  for (auto x : get<0>(hand)) {
    count_value.push_back({x.second, x.first});
  }
  sort(count_value.rbegin(), count_value.rend());



  // cout << "\n" << hand_rank(hand) << endl;
  // for (auto v : count_value) {
  //   cout << get<0>(v) << "-" << get<1>(v) << endl;
  // }



  return {hand_rank(hand), count_value};
}

tuple<map<int, int>, map<string, int>> hand(vector<string> & cards) {

    map<int, int> values;
    map<string, int> suits;

    for (auto c : cards) {
      int value = value_to_int(c[0]);
      string suit = string{c[1]};

      if (values.find(value) == values.end())
        values[value] = 0;
      values[value] += 1;

      if (suits.find(suit) == suits.end())
        suits[suit] = 0;
      suits[suit] += 1;
    }
    return {values, suits};
}

template <typename T>
bool black_vs_white(T black, T white) {

  cout << "black d: " << black << ". white d: " << white << endl;
  if (black > white) {
    cout << "Black wins.\n";
    return true;
  }

  if (black < white) {
    cout << "White wins.\n";
    return true;
  }

  return false;
}

void decide_winner(tuple<double, vector<pair<int, int>>> black, tuple<double, vector<pair<int, int>>> white) {

  if (black_vs_white(get<0>(black), get<0>(white))) {
    return;
  }
  // if () {
  //   cout << "Black wins.\n";
  //   return;
  // }

  // if (get<0>(black) < get<0>(white)) {
  //   cout << "White wins.\n";
  //   return;
  // }

  // auto black_count = get<1>(black);
  // auto white_count = get<1>(white);






  cout << "Tie.\n";
}

int main() {
  string line;
  string card;

  while (getline(cin, line)) {
    stringstream ss(line);

    vector<string> black_cards;
    for (int i = 0; i < 5; i++) {
      ss >> card;
      black_cards.push_back(card);
    }

    vector<string> white_cards;
    for (int i = 0; i < 5; i++) {
      ss >> card;
      white_cards.push_back(card);
    }

    auto black = hand(black_cards);
    auto white = hand(white_cards);

    auto blk_comp = hand_comparator(black);
    auto wht_comp = hand_comparator(white);



    decide_winner(blk_comp, wht_comp);



  }
}
