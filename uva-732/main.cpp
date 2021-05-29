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

using namespace std;

void move(stack<int> & atrain, stack<int> & station) {
  station.push(atrain.top());
  atrain.pop();
}

int main() {

  int coaches;
  while (cin >> coaches) {
    if (coaches == 0) {
      continue;
    }

    string line;
    getline(cin, line);
    getline(cin, line);

    while (line != "0") {

      vector<int> order;
      int car;
      istringstream iss(line);
      for (int i = 0; i < coaches; i++) {
        iss >> car;
        order.push_back(car);
      }

      stack<int> atrain;
      for (int i = coaches; i >= 1; i--) {
        atrain.push(i);
      }

      string output = "Yes";
      stack<int> station;
      station.push(0);

      for (auto car : order) {

        while (station.top() != car) {
          if (atrain.empty()) break;

          move(atrain, station);
        }

        if (station.top() != car) {
          output = "No";
          break;
        }

        station.pop();
      }

      cout << output << endl;
      getline(cin, line);
      if (line == "0") cout << endl;
    }
  }

}
