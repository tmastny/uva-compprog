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

int modexp(int x, int y, int N) {
    if (y == 0) return 1;
    int z = modexp(x, y / 2, N);

    if (y % 2 == 0) {
        return z * z % N;
    }

    return x * z * z % N;
}

int main() {
    auto e = extended_euclidean(25, 11);

    cout << e.x << " " << e.y << endl;

    cout << gcd(25, 11) << endl;
    cout << inverse(11, 25) << endl;

    cout << inverse(2, 127) << endl;


    cout << endl;
    cout << "Problem 1.27" << endl;

    int public_key = 391;
    int encoded_message = (41*41*41 % public_key);
    cout << encoded_message << endl;

    int secret_decoder = inverse(3, (17 - 1) * (23 - 1));
    cout << secret_decoder << endl;

    int decoded_message = modexp(encoded_message, secret_decoder, public_key);
    cout << decoded_message << endl;

    cout << endl;
    cout << "Problem 1.28" << endl;

    int p = 7;
    int q = 11;
    int N = 7 * 11;

    // does the usual `3` work?
    cout << gcd(3, (p - 1) * (q - 1)) << endl;
    cout << gcd(7, (p - 1) * (q - 1)) << endl;

    cout << "Public keys: (" << N << ", " << 7 << ")" << endl;

    cout << "Secret key: " << inverse(7, (p - 1) * (q - 1)) << endl;
}
