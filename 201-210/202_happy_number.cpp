

/*
202. Happy Number (https://leetcode.com/problems/happy-number/description/?envType=study-plan-v2&envId=top-interview-150)

create a function that calculates the square of sum of digits in a number
    repeatedly adds up (n%10)^2 and divide n/10 to get the sum of the digits
    
repeatedly call the function on n, storing each computed value into a hash set
    if 1 is computed, return that n is a happy number
    check every computed value if it exists in the hash set, if true, there is a cycle 
        since we return true at the first sight of 1, we know this cycle does not contain a 1, and is not a happy number
            its a sad number :(

runtime: O(log_10(n)), squareSum is log_10(n), rest of the algorithm can be treated as O(1)
    probably some math reason to prove that repeatedly adding the squares of each digit is constant time
space: O(1)

*/

#include <iostream>
#include <unordered_set>
using namespace std;

int squareSum(int n) {
    int total = 0;
    while (n > 0) {
        total += (n % 10) * (n % 10);
        n /= 10;
    }
    return total;
}

bool isHappy(int n) {
    unordered_set<int> visited;

    while (n != 1) {
        // cout << n << endl;

        if (visited.count(n)) {
            return false;
        }
        visited.insert(n);
        n = squareSum(n);
    }
    return true;
}

int main() {

    int n = 19;

    cout << isHappy(n) << endl;

    return 0;
}