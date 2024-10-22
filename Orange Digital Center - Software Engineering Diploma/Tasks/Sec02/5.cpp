#include <iostream>
using namespace std;

int main(){
    int num, res = 1;
    cout<<"Enter Number: ";
    cin>>num;
    for(int i = num; i >= 1; i--){
        res = res * i;
    }
    cout<<"Factorial Is: "<< res;
    return 0;
}