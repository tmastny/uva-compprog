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

// pow is not working with long long
// That's because I need a 1,000,000 bits,
// not just a representation that equals that value

// Can I use bit shifts instead? That's equivalent right?

// b << n <==> b * 2^n


unsigned long long  calc_interval(unsigned long long left, unsigned long long right) {
  return (
    (pow(2, right + 1) - 1) - (pow(2, 1 + left) - 1)
  );
}

int main() {

  int onetime, repeating;

  while (cin >> onetime >> repeating) {
    if (onetime == 0 && repeating == 0) break;


    vector<pair<unsigned long long , unsigned long long >> times;
    for (int i = 0; i < onetime; i++) {
      unsigned long long start, end;
      cin >> start >> end;

      times.push_back({start, end});
    }

    for (int i = 0; i < repeating; i++) {
      unsigned long long start, end, interval;
      cin >> start >> end >> interval;

      while (end < 1000000) {
        times.push_back({start, end});
        start += interval;
        end += interval;
      }
    }

    string output = "NO CONFLICT";
    unsigned long long availability = 0;
    for (auto t : times) {
      unsigned long long last_availability = availability;

      cout << availability << endl;
      cout << t.first << " " << t.second << endl;
      availability ^= calc_interval(t.first, t.second);

      if ((availability & last_availability) != last_availability) {
        output = "CONFLICT";
        break;
      }
    }
    cout << availability << endl;

    cout << output << endl;

  }

  unsigned long long t = pow(2, 100);
  cout << t << endl;

}
