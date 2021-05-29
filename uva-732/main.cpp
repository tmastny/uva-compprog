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

class Stack {
  public:
    string sequence;
    stack<char> stack;

    void push(char c) {
      stack.push(c);
      sequence.push_back('i');
    };
    void pop() {
      stack.pop();
      sequence.push_back('o');
    };
    Stack() {
      stack.push('!');
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
    while (s.stack.top() != t) {
      if (source.empty()) break;

      s.push(source.front());
      source.pop_front();
    }

    if (s.stack.top() != t) {
      is_anagram = false;
      break;
    }

    // deque source;
    // if (in_queue(source, t))
    if (source.front() == t) {
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

    for (auto s : sequences) {
      for (auto c : s) {
        cout << c << " ";
      }
      cout << endl;
    }

    i++;
    if (i > 2)
      break;
  }

}
