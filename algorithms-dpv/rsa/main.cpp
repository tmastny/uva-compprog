#include <vector>
#include <set>
#include <iostream>

using namespace std;

struct EuclidStep {
    int x;
    int y;
    int d;
};

EuclidStep extended_euclidean(int a, int b) {
    if (b == 0) return EuclidStep {1, 0, a};

    auto result = extended_euclidean(b, a % b);

    return EuclidStep {result.y, result.x - a / b * result.y, result.d};
}

int gcd(int a, int b) {
    return extended_euclidean(a, b).d;
}

int inverse(int a, int N) {
    return (N + extended_euclidean(a, N).x) % N;
}

int main() {
    auto e = extended_euclidean(25, 11);

    cout << e.x << " " << e.y << endl;

    cout << gcd(25, 11) << endl;
    cout << inverse(11, 25) << endl;
}
