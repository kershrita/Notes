#include <iostream>
using namespace std;

int main(){
    int num, checker;
    cout<<"Enter Number You want To Check: ";
    cin>> num;
    for(int i = 1; i <= num; i++){
        if(num % i == 0){
            checker++;
        }
    }
    if(checker == 2){
        cout<<"This Number Is Prime!";
    }else{
        cout<<"This Not Prime Number!";
    }
    return 0;
}