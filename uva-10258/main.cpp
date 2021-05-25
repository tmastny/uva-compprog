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
    bool attempted = false;

    Contestant(int id);
    void update(int problem, int time, string outcome);
};

bool operator<(const Contestant &c1, const Contestant &c2) {

  if (c1.correct < c2.correct) return true;
  if (c1.correct > c2.correct) return false;

  if (c1.penalty < c2.penalty) return false;
  if (c1.penalty > c2.penalty) return true;

  if (c1.id < c2.id) return false;
  if (c1.id > c2.id) return true;

  return false;
}

Contestant::Contestant(int id) : id(id) {}

void Contestant::update(int problem, int time, string outcome) {
  attempted = true;

  if (outcome == "I") {
    problem_penalty[problem] += 20;
    return;
  }

  if (outcome == "C") {
    correct++;
    penalty += problem_penalty[problem] + time;
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

    int contestant, problem, time;
    string outcome;


    vector<Contestant*> scores;
    for (int i = 0; i <= 100; i++) {
      scores.push_back(new Contestant(i));
    }


    getline(cin, line);
    while (!line.empty()) {
      istringstream ss(line);
      ss >> contestant >> problem >> time >> outcome;

      scores[contestant]->update(problem, time, outcome);


      getline(cin, line);
    }

    sort(scores.rbegin(), scores.rend(),
      [](Contestant* c1, Contestant* c2) { return *c1 < *c2; }
    );

    for (auto c : scores) {
      if (c->attempted)
        cout << c->id << " " << c->correct << " " << c->penalty << endl;
    }


    cout << endl;
  }



}
