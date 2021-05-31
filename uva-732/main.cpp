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
#include <bitset>
#include <list>
#include <stack>
#include <queue>
#include <deque>

using namespace std;

// depth first search:
// - go as far as possible in the branch before backtracking
//
// That is the approach I used in this problem. I may recruse deeper,
// but I always return to the last recursion point before continuing
// down other branches.




// Optimization: https://www.redgreencode.com/implementing-a-fast-solution-to-uva-732/
// - pruning via recursion found to be best
// - I did vaguely consider brute forcing it, but recrusion felt right
//   because there was forced sequences, and potential branches.

class Stack {
  public:
    string sequence;
    stack<char> stk;

    void push(char c) {
      stk.push(c);
      sequence.push_back('i');
    };
    void pop() {
      stk.pop();
      sequence.push_back('o');
    };
    Stack() {
      stk.push('!');
    }
};

bool in_queue(deque<char> q, char c) {
  return find(q.begin(), q.end(), c) != q.end();
}

void check_anagram(
  vector<string> & sequences, Stack s, deque<char> source, queue<char> target,
  bool is_recurse
) {

  if (is_recurse) {
    s.push(source.front());
    source.pop_front();
  }


  bool is_anagram = true;
  while (!target.empty()) {

    auto t = target.front();
    while (s.stk.top() != t) {
      if (source.empty()) break;

      s.push(source.front());
      source.pop_front();
    }

    if (s.stk.top() != t) {
      is_anagram = false;
      break;
    }

    if (in_queue(source, t)) {
      check_anagram(sequences, s, source, target, true);
    }

    s.pop();
    target.pop();
  }

  if (is_anagram)
    sequences.push_back(s.sequence);

}


int main() {

  string source, target;
  int i = 1;
  while (getline(cin, source)) {
    getline(cin, target);



    deque<char> qsource;
    for (auto s : source)
      qsource.push_back(s);

    queue<char> qtarget;
    for (auto t : target)
      qtarget.push(t);


    vector<string> sequences;
    Stack s;
    check_anagram(sequences, s, qsource, qtarget, false);

    sort(sequences.begin(), sequences.end());

    cout << "[" << endl;
    for (auto s : sequences) {
      for (auto c : s) {
        cout << c << " ";
      }
      cout << endl;
    }
    i++;
    cout << "]" << endl;
  }

}
