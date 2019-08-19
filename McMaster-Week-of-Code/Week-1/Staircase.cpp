#include <bits/stdc++.h>

using namespace std;

// Complete the staircase function below.
void staircase(int n) {
    char output[100];
    
    for (int i = 0; i < n; ++i) {
        output[i] = ' ';
    }
    output[n] = 0;
    
    for (int i = n-1; i >= 0; --i) {
        output[i] = '#';
        cout << output << endl;
    }
}

int main()
{
    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    staircase(n);

    return 0;
}
