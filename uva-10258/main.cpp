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

using namespace std;

class Contestant {
  private:
    map<int, int> problem_penalty {{1, 0}, {2, 0}, {3, 0},
      {4, 0}, {5, 0}, {6, 0}, {7, 0}, {8, 0}, {9, 0}
    };

  public:
    int correct = 0;
    int penalty = 0;
    int id;

    Contestant(int id);
    void update(int problem, int time, string outcome);
};

Contestant::Contestant(int id) : id(id) {}

void Contestant::update(int problem, int time, string outcome) {

  if (outcome == "I") {
    problem_penalty[problem] = 20;
    return;
  }

  if (outcome == "C") {
    correct++;
    penalty = problem_penalty[problem] + time;
    return;
  }
}

int main() {



  string line;
  getline(cin, line);

  istringstream ss(line);

  int cases;
  ss >> cases;

  getline(cin, line);

  while (cases--) {

    cout << cases << endl;

    int contestant, problem, time;
    string outcome;


    map<int, Contestant*> scores;
    for (int i = 1; i <= 100; i++) {
      scores[i] = new Contestant(i);
    }


    getline(cin, line);
    while (!line.empty()) {
      istringstream ss(line);
      ss >> contestant >> problem >> time >> outcome;
      cout << outcome << endl;

      getline(cin, line);
    }


    cout << endl;
  }



}
