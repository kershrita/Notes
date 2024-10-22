#include <iostream>
using namespace std;

int main(){
    int num1, num2, gcd;
    cout<<"Enter Number 1: ";
    cin>> num1;
    cout<<"Enter Number 2: ";
    cin>> num2;
    if(num1 < num2){
        int tmp;
        tmp = num1;
        num1 = num2;
        num2 = tmp;
    }
    for(int i = 1; i <= num1; i++){
        if(num1 % i == 0 && num2 % i == 0){
            gcd = i;
        }
    }
    cout<<"GCD Is: " << gcd << endl;
    return 0;
}