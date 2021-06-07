#include <vector>
#include <map>
#include <iostream>

using namespace std;

//  Naive solution:
//      For each element of haystack, check if
//      the next `n` elements of haystack form
//      the needle string.

//      Complexity: O(h * n)

//  Optimal solution: Knuth-Morris-Pratt (KMP) Algorithm
//      Complexity: O(h + n)



class Solution {
public:
    int strStr(string haystack, string needle) {
        if (needle == "") return 0;

        for (int h = 0; h < haystack.size(); h++) {

            int n = 0;
            while (n < needle.size() && h + n < haystack.size()) {

                if (needle[n] != haystack[h + n]) break;
                n++;
            }

            if (n == needle.size()) {
                return h;
            }
        }

        return -1;
\ bbvn];

int main() {

}
