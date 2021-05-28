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

using namespace std;

int calc_interval(int left, int right) {
  return (
    (pow(2, right) - 1) - (pow(2, 1 + left) - 1)
  );
}

int main() {

  int onetime, repeating;

  while (cin >> onetime >> repeating) {
    if (onetime == 0 && repeating == 0) break;


    vector<pair<int, int>> times;
    for (int i = 0; i < onetime; i++) {
      int start, end;
      cin >> start >> end;

      times.push_back({start, end});
    }

    sort(times.begin(), times.end());


    for (int i = 0; i < repeating; i++) {
      int start, end, interval;
      cin >> start >> end >> interval;
    }

    string output = "NO CONFLICT";
    for (int i = 0; i < times.size() - 1; i++) {
      if (times[i].second > times[i + 1].first) {
        output = "CONFLICT";
      }
    }
    cout << output << endl;

    for (auto t : times) {
      cout << "[" << t.first << ", " << t.second << "] ";
    }
    cout << endl;

  }

}
