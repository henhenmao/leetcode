

/*
1518. Water Bottles (https://leetcode.com/problems/water-bottles/description/)

either just do a iterative simulation or recursion simulation to find the maximum water bottles

while you have water bottles, drink all that you have
    let n be the number of water bottles you have
    drink n water bottles -> add to the total
    n // numExchange (floor divide) is the number of water bottles you can exchange for
    add n // numExchange to n after adding n to the total

algorithm:
    1. numBottles = current full bottles, emptyBottles = current empty bottles
    2. drink all current full bottles -> totalDrank += numBottles
    3. add the number of bottles drank to emptyBottles -> emptyBottles += numBottles at the same time
    4. exchange as many empty bottles you can -> numBottles = emptyBottles / numExchange
    5. update emptyBottles to remainder after exchange -> emptyBottles %- numExcahnge

runtime: O(log_k(n)), where n is numBottles, and k is numExchange
    we are dividing numBottles by at least numExchange until numBottles is full
    this results in an log base numExchange of numBottles

space: O(1)

*/

#include <iostream>
using namespace std;


int numWaterBottles(int numBottles, int numExchange) {
    int totalDrank = 0;
    int emptyBottles = 0;

    while (numBottles) {
        totalDrank += numBottles;
        emptyBottles += numBottles;
        numBottles = emptyBottles / numExchange;
        emptyBottles %= numExchange;
    }
    return totalDrank;
}

int main() {
    cout << numWaterBottles(15, 4) << endl;

    return 0;
}