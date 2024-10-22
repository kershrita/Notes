#include <iostream>
using namespace std;

void prime(int num) {
    int checker = 0;
    for (int i = 1; i <= num; i++) {
        if (num % i == 0) {
            checker++;
        }
    }
    if (checker == 2) {
        cout << "This Number Is Prime!";
    }
    else {
        cout << "This Not Prime Number!";
    }
}
int main() {
    int n;
    cout << "Enter Number You want To Check: ";
    cin >> n;
    prime(n);
    return 0;
}