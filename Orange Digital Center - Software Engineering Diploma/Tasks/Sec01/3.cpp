#include <iostream>
using namespace std;

int main(){
    int quantity, cost;

    cout<<"How Many Units: ";
    cin>> quantity;
    
    cost = 100 * quantity;

    if(cost >= 1000){
        cost = cost - 0.1 * cost;
        cout<<"Total Cost: "<< cost;
    }else{
        cout<<"Total Cost: "<< cost;
    }

    return 0;
}