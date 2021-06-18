#include <cstdio>
#include <algorithm>

using namespace std;

int cycle_length(int n) {
  int cycle_length = 1;

  while (n != 1) {
    if (n % 2 == 0) {
      n = n / 2;
    } else {
      n = 3 * n + 1;
    }
    cycle_length++;
  }

  return cycle_length;
}

int main() {
  int i, j = 1;

  while (scanf("%d %d", &i, &j) != EOF) {

    int max_cycle_length = 1;
    int current_cycle_length = 1;
    for (int k = min(i, j); k <= max(i, j); k++) {
      current_cycle_length = cycle_length(k);

      if (current_cycle_length > max_cycle_length) {
        max_cycle_length = current_cycle_length;
      }
    }

    printf("%d %d %d\n", i, j, max_cycle_length);
  }
}
