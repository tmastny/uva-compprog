#include <cstdio>

using namespace std;

int main() {
  int a, b, c = 1;

  while (scanf("%d %d", &a, &b) != EOF) {
    if (c > 1) printf("\n");
    printf("Case %d: %d\n", c++, a + b);
  }
}
