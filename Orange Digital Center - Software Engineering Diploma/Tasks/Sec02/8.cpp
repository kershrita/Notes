#include <iostream>
using namespace std;

int main(){
    int num, tmp, sum;
    cout<<"Enter Your Number: ";
    cin>> num;
    while(num > 0){
        tmp = num % 10;
        sum = sum + tmp;
        num = num / 10;
    }
    cout<<"Sum Of Digits: "<< sum << endl;
    return 0;
}