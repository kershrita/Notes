#include <iostream>
using namespace std;

void mult(int array1[2][3], int array2[3][2]){
    int r_arr1 = 2, c_arr1 = 3, r_arr2 = 3, c_arr2 = 2;
    int res[2][2];
    if (c_arr1 == r_arr2) {
        int multiply = 0;

        for (int p = 0; p < c_arr2; p++) {

            for (int i = 0; i < r_arr1; i++) {

                for (int j = 0; j < r_arr2; j++) {

                    multiply += array1[p][j] * array2[j][i];
                    
                }

                res[p][i] = multiply;
                multiply = 0;
            }

        }

    }
    else {
        cout << "Can't Multiply!";
    }
    cout << "{";
    for (int i = 0; i < r_arr1; i++) {
        for (int j = 0; j < c_arr2; j++) {
            cout << res[i][j];
            if (res[i][j] != res[1][1]) {
                cout << ", ";
            }
        }
        if (res[i] != res[1]) {
            cout << endl;
        }
    }
    cout << "}";
}

int main() {
    int arr1[2][3] = {
        1, 2, 3,
        4, 5, 6
    };
    int arr2[3][2] = {
        7, 8,
        9, 10,
        11, 12
    };
    mult(arr1, arr2);
    return 0;
}
