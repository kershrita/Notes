#include <iostream>
using namespace std;

void hello() {
    cout << "hello";
}

void sayHello() {
    hello();
}

int main() {
    sayHello();
    return 0;
}
