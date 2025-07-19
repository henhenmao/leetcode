


#include <iostream>
#include <vector>

using namespace std;


int main() {
    string s = "abcde";
    
    for (int i = 0; i < s.length(); i++) {
        cout << s.substr(0, i) + s.substr(i+1) << endl;
    }

    return 0;
}