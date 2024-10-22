#include <iostream>
using namespace std;

int main(){
    int salary, years;
    double bonus;

    cout<<"What's Your Salary: ";
    cin>> salary;
    cout<<"How Many Years Have You Been Working Here: ";
    cin>> years;

    if(years >= 5){
        bonus = 0.05 * salary;
        salary = salary + bonus;
        cout<<"Your New Salary Is: "<< salary <<", With Net Bonus Amount: "<< bonus;
    }else{
        cout<<"Your Salary Is: "<< salary <<", With No Bonus";
    }

    return 0;
}