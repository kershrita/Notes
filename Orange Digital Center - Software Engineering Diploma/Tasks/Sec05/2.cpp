#include <iostream>
using namespace std;

int main() {
    int arr[10] = {60, 56, 81, 3, 45, 12, 10, 34, 8, 1};
    int tmp;
    for (int i = 0; i < 10; i++) {
        for (int j = i+1; j < 10; j++) {
            if (arr[i] < arr[j]) {
                tmp = arr[i];
                arr[i] = arr[j];
                arr[j] = tmp;
            }
        }
    }
    cout << arr[1];
    return 0;
}
