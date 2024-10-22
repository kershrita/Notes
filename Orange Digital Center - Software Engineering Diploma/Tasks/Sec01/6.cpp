#include <iostream>
using namespace std;

int main(){
    int user_age1, user_age2, user_age3;

    cout<<"Enter User Age One: ";
    cin>> user_age1;
    cout<<"Enter User Age Two: ";
    cin>> user_age2;
    cout<<"Enter User Age Three: ";
    cin>> user_age3;

    if(user_age1 > user_age2 && user_age1 > user_age3){
        cout<<"The Age Of Oldest User Is: "<< user_age1;
        if(user_age2 < user_age3){
            cout<<", And Youngest User Is: " << user_age2;
        }else{
            cout<<", And Youngest User Is: " << user_age3;
        }
    }else if(user_age2 > user_age1 && user_age2 > user_age3){
        cout<<"The Age Of Oldest User Is: "<< user_age2;
        if(user_age1 < user_age3){
            cout<<", And Youngest User Is: " << user_age1;
        }else{
            cout<<", And Youngest User Is: " << user_age3;
        }
    }else if(user_age3 > user_age1 && user_age3 > user_age2){
        cout<<"The Age Of Oldest User Is: "<< user_age3;
        if(user_age1 < user_age2){
            cout<<", And Youngest User Is: " << user_age1;
        }else{
            cout<<", And Youngest User Is: " << user_age2;
        }
    }
    return 0;
}