#include <iostream>
using namespace std;

int main() {
    int arr[10] = { 60, 56, 81, 3, 45, 12, 10, 34, 8, 1 };
    int sum = 0;
    for (int i = 9; i >= 0; i--) {
        cout << arr[i] << " ";
    }
    return 0;
}

