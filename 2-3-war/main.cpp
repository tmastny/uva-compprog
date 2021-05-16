#include <random>
#include <cstdio>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <set>

using namespace std;

auto rng = default_random_engine {};

queue<int> make_deck() {
  vector<int> deck;
  for (int s = 1; s <= 2; s++) {
    for (int i = 2; i <= 14; i++) {
      deck.push_back(i);
    }
  }

  shuffle(deck.begin(), deck.end(), rng);

  queue<int> qdeck;
  for (auto i : deck)
    qdeck.push(i);

  return qdeck;
}

int war(queue<int> &d1, queue<int> &d2) {
  int moves = 0;
  // without shuffling ties, they expected value may be infinite:
  // https://boardgames.stackexchange.com/questions/44275/what-is-the-expected-duration-of-a-game-of-war/44292
  // so I will use a vector instead of a stack
  stack<int> ties;
  //vector<int> ties;

  while (!d1.empty() && !d2.empty()) {
    moves++;

    // cout << "score: " << d1.size() << " - " << d2.size() << " r: " << ties.size() << endl;

    int c1 = d1.front();
    int c2 = d2.front();

    // cout << c1 << " vs. " << c2 << endl;

    d1.pop();
    d2.pop();

    queue<int> * winner;
    if (c1 > c2) {
      winner = &d1;
    } else if (c1 < c2) {
      winner = &d2;
    } else {
      ties.push(c1);
      ties.push(c2);

      if (d1.empty() || d2.empty()) break;

      ties.push(d1.front());
      ties.push(d2.front());
      d1.pop();
      d2.pop();

      continue;
    }

    winner->push(c1);
    winner->push(c2);

    int c;
    while (!ties.empty()) {
      c = ties.top();
      ties.pop();
      winner->push(c);
    }
  }

  return moves;
}

int main() {

  vector<int> moves;
  for (int i = 0; i < 4; i++) {
    queue<int> d1 = make_deck();
    queue<int> d2 = make_deck();

    moves.push_back(war(d1, d2));
  }

  double total = 0;
  for (auto i : moves) {
    total += i;
  }
  printf("%.2f\n", total / moves.size());
}
