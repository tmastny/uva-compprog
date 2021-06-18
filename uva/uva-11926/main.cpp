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

bool has_conflict(bitset<1000001> & bits, int start, int end) {
  for (int i = start; i < end; i++) {
    if (bits[i]) return true;
    bits.set(i);
  }

  return false;
}

int main() {

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

  bitset<1000001> availability;
  int onetime, repeating;

  while (cin >> onetime >> repeating, onetime || repeating) {
    availability.reset();


    string output = "NO CONFLICT";
    for (int i = 0; i < onetime; i++) {
      int start, end;
      cin >> start >> end;


      if (has_conflict(availability, start, end)) {
        output = "CONFLICT";
        break;
      }
    }

    for (int i = 0; i < repeating; i++) {
      if (output == "CONFLICT") break;

      int start, end, interval;
      cin >> start >> end >> interval;

      while (end <= 1000000) {
        if (has_conflict(availability, start, end)) {
          output = "CONFLICT";
          break;
        }

        start += interval;
        end += interval;
      }
    }

    cout << output << endl;
  }
}
