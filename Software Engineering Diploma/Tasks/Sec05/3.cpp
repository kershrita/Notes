#include <iostream>
using namespace std;

int main() {
    int arr[10] = {60, 56, 81, 3, 45, 12, 10, 34, 8, 1};
    int tmp, range;
    for (int i = 0; i < 10; i++) {
        for (int j = i+1; j < 10; j++) {
            if (arr[i] < arr[j]) {
                tmp = arr[i];
                arr[i] = arr[j];
                arr[j] = tmp;
            }
        }
    }
    cout << "Enter The N Largest Elements In Range 1 To 10: ";
    cin >> range;
    for (int i = range-1; i >= 0; i--) {
        cout << arr[i] << " ";
    }
    return 0;
}
