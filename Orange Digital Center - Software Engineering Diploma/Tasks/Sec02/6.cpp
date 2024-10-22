#include <iostream>
using namespace std;

int main(){
    int base, power, res = 1;
    cout<<"Enter Base Number: ";
    cin>>base;
    cout<<"Enter Power Number: ";
    cin>>power;
    for(int i = power; i >= 1; i--){
        res = res * base;
    }
    cout<<"Your Number Is: "<< res;
    return 0;
}