#include <iostream>
using namespace std;

int main(){
    int held_classes, attended_classes;
    double percentage;

    cout<<"How Many Classes Are Held: ";
    cin>> held_classes;
    cout<<"How Many Classes Are Attended: ";
    cin>> attended_classes;

    percentage = (attended_classes * 100) / held_classes;
    cout<<"Your Percentage Of Attending Is: " << percentage <<"%"<< endl;

    if(percentage >= 75){
        cout<<"You Are Allowed To Sit In Exam";
    }else{
        cout<<"You Aren't Allowed To Sit In Exam";
    }
    
    return 0;
}