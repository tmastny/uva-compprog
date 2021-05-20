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

using namespace std;

int gcd(int a, int b) {
  int temp;
  while(b != 0) {
    temp = b;
    b = a % b;
    a = temp;
  }

  return a;
}

int lcm(int a, int b) {
  return a * b / gcd(a, b);
}

int main() {
  int cases;
  cin >> cases;

  for (int c = 0; c < cases; c++) {

    int days;
    int parties;

    cin >> days;
    cin >> parties;

    int hartal; // average number of days between successive strikes
    set<int> unique_hartals;
    for (int i = 0; i < parties; i++) {
      cin >> hartal;
      unique_hartals.insert(hartal);
    }

    vector<int> hartals;
    for (auto h : unique_hartals) {
      hartals.push_back(h);
    }




    int total = 0;
    for (auto h : hartals) {
      total += days / h;
    }

    for (int i = 0; i < hartals.size(); i++) {
      for (int j = i; j < hartals.size(); j++) {
        if (i == j) continue;

        int a = hartals[i];
        int b = hartals[j];

        // cout << "days: " << days << " " << a << "-" << b << " lcm: " << lcm(a, b) << endl;

        total -= days / lcm(hartals[i], hartals[j]);
      }
    }
    cout << "before weekend: " << total << endl;
    set<int> on_friday;
    int on_saturday = 0;
    for (auto h : hartals) {
      total -= days / lcm(h, 7);


      for (int i = 6; i <= days; i = i + 7) {

        if (lcm(h, i) == i)
          on_friday.insert(i);
      }

    }
    total -= on_friday.size();

    cout << total << endl;



  }
  for (int i = 1; i <= 28; i++) {
    printf("%02.0d ", i);
  }
  cout << endl;

  for (int i = 1; i <= 28; i++) {

    int o = 0;
    if (i % 2 == 0) o = 1;
    printf("%02.0d ", o);
  }
  cout << endl;

  for (int i = 1; i <= 28; i++) {
    int o = 0;
    if (i % 4 == 0) o = 1;
    printf("%02.0d ", o);
  }
  cout << endl;
}
