#include <vector>
#include <iostream>
#include <map>

using namespace std;

class Solution {
public:
    map<int, int> freq(vector<int> & n) {

        map<int, int> s;
        for (auto i : n) {
            if (s.find(i) == s.end()) {
                s[i] = 0;
            }

            s[i]++;
        }

        return s;
    }

    void add_element(vector<int> & n, int element, int times) {

        for (int i = 0; i < times; i++) {
            n.push_back(element);
        }
    }

    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        auto m1 = freq(nums1);
        auto m2 = freq(nums2);

        vector<int> intersect;
        for (auto x : m1) {

            auto it = m2.find(x.first);
            if (it != m2.end()) {
                add_element(intersect, it->first, min(x.second, it->second));
            }
        }

        return intersect;
    }
};
int main() {


  vector<int> t1 {7, 1, 5, 3, 6, 4};
  vector<int> t2 {1, 2, 3, 4, 5};
  vector<int> t3 {7, 6, 4, 3, 1};

  Solution s;

  for (auto i : s.intersect(t1, t2)) {
      cout << i << endl;
  }
}
