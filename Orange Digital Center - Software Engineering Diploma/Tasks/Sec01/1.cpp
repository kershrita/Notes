#include <iostream>
using namespace std;

int main(){
    int length, width;

    cout<<"Enter Length of Rectangle: ";
    cin>> length;
    cout<<"Enter Width of Rectangle: ";
    cin>> width;

    if(length == width){
        cout<<"Square";
    }else{
        cout<<"Not Square";
    }
    
    return 0;
}