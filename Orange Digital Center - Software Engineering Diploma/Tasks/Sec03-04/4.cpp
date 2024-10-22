#include <iostream>
using namespace std;

void factors(int num) {
    int checker = 0;
    for (int i = 1; i <= num; i++) {
        if (num % i == 0) {
            cout << i << " ";
        }
    }
}
int main() {
    int n;
    cout << "Enter Number You want To Check: ";
    cin >> n;
    factors(n);
    return 0;
}
