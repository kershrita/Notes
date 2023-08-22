#include <iostream>
using namespace std;

int main(){
    double marks;

    cout<<"What's Your Mark: ";
    cin>> marks;

    if(marks >= 80){
        cout<<"Your Grade Is: A";
    }else if(marks >= 60 && marks < 80){
        cout<<"Your Grade Is: B";
    }else if(marks >= 50 && marks < 60){
        cout<<"Your Grade Is: C";
    }else if(marks >= 45 && marks < 50){
        cout<<"Your Grade Is: D";
    }else if(marks >= 25 && marks < 45){
        cout<<"Your Grade Is: E";
    }else{
        cout<<"Your Grade Is: F";
    }

    return 0;
}