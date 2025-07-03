

/*
3100. Water Bottles II (https://leetcode.com/problems/water-bottles-ii/description/)

In one operation, you can perform one of the following operations:
    Drink any number of full water bottles turning them into empty bottles.
    Exchange numExchange empty bottles with one full water bottle. Then, increase numExchange by one.

i do not know the point of letting us choose any number of full water bottles
    pretty sure that it's always beneficial to drink every water bottle you have at any given operation

algorithm:
    1. drink every water bottle you have
    2. if no full water bottles left, exchange for one bottle and increment numExchange
    3. repeat two previous steps

i have no idea what the runtime for this is

*/

#include <iostream>
using namespace std;

int maxBottlesDrunk(int numBottles, int numExchange) {
    int totalDrank = 0;
    int emptyBottles = 0;

    while (numBottles) {
        totalDrank += numBottles;
        emptyBottles += numBottles;
        numBottles = 0;

        if (emptyBottles >= numExchange) {
            emptyBottles -= numExchange;
            numBottles++;
            numExchange++;
        }
    }

    return totalDrank;
}


// int main() {
//     cout << maxBottlesDrunk(10,3) << endl;
//     return 0;
// }