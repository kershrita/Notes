#include <iostream>
using namespace std;

double fact(double num) {
    double res = 1;
    for (double i = num; i >= 1; i--) {
        res = res * i;
    }
    return res;
}

int main() {
    double n;
    cout << "Enter Number : ";
    cin >> n;
    double out = fact(n);
    cout << "Factorial Is: " << out;
    return 0;
}