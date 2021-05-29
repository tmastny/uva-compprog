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

void check_anagram(
  vector<string> & sequences, Stack s, queue<char> source, queue<char> target
) {

  bool is_anagram = true;
  while (!target.empty()) {

    auto t = target.front();
    while (s.stack.top() != t) {
      if (source.empty()) break;

      s.push(source.front());
      source.pop();

      // if (source.front() == t) {

      // }
    }

    if (s.stack.top() != t) {
      is_anagram = false;
      break;
    }

    s.pop();
    target.pop();
  }

  if (is_anagram)
    sequences.push_back(s.sequence);

}


int main() {

  string source, target;

  while (getline(cin, source)) {
    getline(cin, target);



    queue<char> qsource;
    for (auto s : source)
      qsource.push(s);

    queue<char> qtarget;
    for (auto t : target)
      qtarget.push(t);


    vector<string> sequences;
    Stack s;
    check_anagram(sequences, s, qsource, qtarget);

    sort(sequences.begin(), sequences.end());

    for (auto s : sequences) {
      for (auto c : s) {
        cout << c << " ";
      }
      cout << endl;
    }


    break;
  }

}
