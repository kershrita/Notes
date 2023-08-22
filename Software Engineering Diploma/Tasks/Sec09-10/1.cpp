// Main 

#include <iostream>
#include "car.h"
using namespace std;

int main() {
    car c1, c2;
    
    c1.type = "BMW";
    c1.color = "Black";

    c2.type = "KIA";
    c2.color = "White";

    return 0;
}

// Class

#include <iostream>
using namespace std;
class car
{
public:
	string type, color;
};


