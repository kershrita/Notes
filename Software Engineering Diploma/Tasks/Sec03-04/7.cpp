#include <iostream>
using namespace std;

void swap(int x, int y) {
    x = x * y;
    y = x / y;
    x = x / y;

    cout << "X Value Now: " << x << endl;
    cout << "Y Value Now: " << y;
}

int main() {
    int num1, num2;
    cout << "Enter X Value: ";
    cin >> num1;
    cout << "Enter Y Value: ";
    cin >> num2;
    swap(num1, num2);
    return 0;
}