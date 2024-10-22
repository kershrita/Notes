#include <iostream>
using namespace std;

int main() {
    int arr[10] = { 60, 56, 81, 3, 45, 12, 10, 34, 8, 1 };
    int sum = 0;
    for (int i = 0; i < 10; i++) {
        sum = sum + arr[i];
    }
    cout << "Sum: " << sum;
    return 0;
}

