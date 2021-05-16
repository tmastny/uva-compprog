#include <cstdio>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

long long int capture_spend() {
  int dollars, cents;

  scanf("%d.%d", &dollars, &cents);

  long long int ret = dollars * 100 + cents;
  return ret;
}

int main() {
  double students;

  while (cin >> students, students != 0) {

    vector<long long int> expenses;
    for (int i = 0; i < students; i++) {
      expenses.push_back(capture_spend());
    }

    long long int total_spend = 0;
    for (auto i : expenses) {
      total_spend += i;
    }
    double desired_spend_per_student = (double) total_spend / students;


    long long int debt = 0;
    long long int credit = 0;
    for (auto spend : expenses) {

      if (spend > desired_spend_per_student) {
        credit += spend - desired_spend_per_student;
      } else {
        debt += desired_spend_per_student - spend;
      }
    }

    double balance = debt;
    if (credit >= debt) {
      balance = credit;
    }

    printf("$%.2f\n", balance / 100.0);
  }

}
