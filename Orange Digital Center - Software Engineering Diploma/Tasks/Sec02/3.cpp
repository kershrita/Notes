#include <iostream>
using namespace std;

int main(){
    int sum;
    for(int i = 1; i <= 10; i++){
        sum = sum + i;
        cout<< i <<" ";
    }
    cout<<"\nSum of Numbers: "<< sum;
    return 0;
}