#include <iostream>
using namespace std;

int find_gcd(int num1, int num2) {
    int gcd;
    if (num1 < num2) {
        int tmp;
        tmp = num1;
        num1 = num2;
        num2 = tmp;
    }
    if (num1 == num2 * num2) {
        gcd = num1;
        return gcd;
    }
    else if (num2 == num1 * num1) {
        gcd = num2;
        return gcd;
    }
    else {
        for (int i = 1; i <= num1; i++) {
            if (num1 % i == 0 && num2 % i == 0) {
                gcd = i;
            }
        }
        return gcd;
    }
}

int main() {
    int num1, num2;
    cout << "Enter Number 1: ";
    cin >> num1;
    cout << "Enter Number 2: ";
    cin >> num2;
    int out = find_gcd(num1, num2);
    cout << "GCD Is: " << out << endl;
    return 0;
}