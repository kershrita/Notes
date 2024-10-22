#include <iostream>
using namespace std;

int main(){
    double num1, num2;

    cout<<"Enter Number One: ";
    cin>> num1;
    cout<<"Enter Number Two: ";
    cin>> num2;

    if(num1 > num2){
        cout<<"The Greatest Value is: "<< num1;
    }else{
        cout<<"The Greatest Value is: "<< num2;
    }
    
    return 0;
}