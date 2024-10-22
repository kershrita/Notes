#include <iostream>
using namespace std;

int powerNum(int base, int power) {
    if (power >= 1) {
        return base * powerNum(base, power - 1);
    }
}

int main() {
    int x, y;
    cout << "Enter Base Number: ";
    cin >> x;
    cout << "Enter Power Number: ";
    cin >> y;
    int out = powerNum(x, y);
    cout << out;
    return 0;
}