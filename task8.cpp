#include <algorithm>
#include <fstream>
#include <iostream>
#include <vector>

// in C++ because why not 
using namespace std;

int N = 99;

vector<int> forest;
vector<bool> visible(N*N, 0);
vector<int> scenicScore(N*N, 1);

void countVisibleInRow(int start, int offset) {
    int m = -1;
    for (int i=0; i<N; i++) {
        if (forest[start] > m) {
            m = forest[start];
            visible[start] = 1;
        }
        start += offset;
    }
}
int scoreForOffset(int start, int x, int a, int b) {
    int m = forest[start], s = 0;
    start += x;
    while (a <= start && start < b && forest[start] < m) {
        s++;
        start += x;
    }
    if (a <= start && start < b) s++;
    return s;
}

void calculateScores(int start) {
    scenicScore[start] *= scoreForOffset(start, N, 0, N*N);
    scenicScore[start] *= scoreForOffset(start, -N, 0, N*N);
    scenicScore[start] *= scoreForOffset(start, 1, start - (start % N), start - (start % N) + N);
    scenicScore[start] *= scoreForOffset(start, -1, start - (start % N), start - (start % N) + N);

}


int main() {

    ifstream file ("input8");
    if (!file.is_open()) {
        return 1;
    }

    char x;
    while (file >> x){
        forest.push_back((int)x);
    }
    // part 1
    for (int i=0; i<N; i++) {
        countVisibleInRow(i, N);
        countVisibleInRow(N*i, 1);
        countVisibleInRow(N*N-1-i, -N);
        countVisibleInRow(N*i+N-1, -1);
    }
    int sum = 0;
    for (auto x : visible) {
        sum += x;
    }

    cout << sum << "\n";

    // part 2
    for (int i=0; i<N*N; i++) {
        calculateScores(i);
    }
    cout << *max_element(scenicScore.begin(), scenicScore.end()) << "\n";
}
