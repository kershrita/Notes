#include <iostream>
using namespace std;

int main() {
    int arr[3][3] = {1, 2, 3,
                     4, 5, 6,
                     7, 8, 9};
    cout << "==============" << endl 
         << "Before Swaping" << endl 
         << "==============" << endl;
    cout << "{";
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            cout << arr[i][j];
            if (arr[i][j] != arr[2][2]) {
                cout << ", ";
            }
        }
        if (arr[i] != arr[2]) {
            cout << endl;
        }
    }
    cout << "}" << endl;

    int tmp[3][3], newarr[3];
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            tmp[j][i] = arr[i][j];
        }
    }

    cout << "==============" << endl
        << "After Swaping" << endl
        << "==============" << endl;
    cout << "{";
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            cout << tmp[i][j];
            if (tmp[i][j] != tmp[2][2]) {
                cout << ", ";
            }
        }
        if (tmp[i] != tmp[2]) {
            cout << endl;
        }
    }
    cout << "}";
    return 0;
}
