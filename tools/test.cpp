


#include <iostream>
#include <vector>

using namespace std;


int main() {
    int a, b;
    int *p;
    int *q;
    int *r;

    a = b;
    q = &b;
    r = &a;

    a = 3;
    cout << a << endl;
    cout << &a << endl;
    
    
    p = r;
    cout << p << endl;
}