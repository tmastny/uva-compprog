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
    vector<char> sequence;
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
    void print() {
      for (auto s : sequence) {
        cout << s << " ";
      }
      cout << endl;
    }
};


int main() {

  string source, target;

  while (getline(cin, source)) {
    getline(cin, target);



    queue<char> qsource;
    for (auto s : source)
      qsource.push(s);

    Stack s;

    bool is_anagram = true;
    for (auto t : target) {

      while (s.stack.top() != t) {
        if (qsource.empty()) break;

        s.push(qsource.front());
        qsource.pop();
      }

      if (s.stack.top() != t) {
        is_anagram = false;
        break;
      }

      s.pop();
    }

    if (is_anagram)
      s.print();



    break;
  }

}
