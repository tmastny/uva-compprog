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

using namespace std;

// pow is not working with long long
// That's because I need a 1,000,000 bits,
// not just a representation that equals that value

// Can I use bit shifts instead? That's equivalent right?

// b << n <==> b * 2^n

int main() {

  bitset<1000001> availability;
  int onetime, repeating;

  while (cin >> onetime >> repeating) {
    if (onetime == 0 && repeating == 0) break;
    availability.reset();

    vector<pair<int, int>> times;
    for (int i = 0; i < onetime; i++) {
      int start, end;
      cin >> start >> end;

      times.push_back({start, end});
    }

   for (int i = 0; i < repeating; i++) {
      int start, end, interval;
      cin >> start >> end >> interval;

      while (end <= 1000000) {
        times.push_back({start, end});
        start += interval;
        end += interval;
      }
    }

    // sort(times.begin(), times.end());

    string output = "NO CONFLICT";
    for (auto t : times) {

      for (int i = t.first + 1; i <= t.second; i++) {
        if (availability[i]) {
          output = "CONFLICT";
          break;
        }
        availability.set(i);
      }

      if (output == "CONFLICT") break;

    }

    cout << output << endl;
  }
}
