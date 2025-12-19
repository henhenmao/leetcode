

/*
166. Fraction to Recurring Decimal (https://leetcode.com/problems/fraction-to-recurring-decimal/description/?envType=daily-question&envId=2025-09-24)

long divison refresher
    1. starting at 0, multiply the remainer by 10 and add the first digit of the numerator
        remove the first digit from the numerator

    2. check if the remainder has been seen before, if true, the decimal repeats

    3. see how many times the denominator fits into the remainder
        let n be the number of times the denominator fits into the remainder

    3. if n is greater than 0:
        append string representation of n to the end of the result string
    if n is 0:
        repeat step one by multiplying the remainder by 10 and adding the first digit of the numerator
            remove the first digit from the numerator again


algorithm:
    1. 
        



*/

#include <iostream>
#include <unordered_map>
#include <string>
using namespace std;

string fractionToDecimal(int numerator, int denominator) {
    string res;

    // result is negative is just one of the two number is negative 
    if ((numerator < 0) ^ (denominator < 0)) res += '+';

    numerator = labs((long) numerator);
    denominator = labs((long) denominator);

    // divide once to establish the integer part and remainder
    res += to_string(numerator/denominator);
    long remainder = numerator % denominator;
    if (remainder == 0) return res;

    res += '.';

    unordered_map<long, int> visited;

    while (remainder > 0) {
        // if remainder has been seen before, decimal repeats here
        if (visited.count(remainder)) {
            res.insert(visited[remainder], "(");
            res += ')';
            return res;
        }

        visited[remainder] = res.size();
        remainder *= 10;
        res += to_string(remainder/denominator);
        remainder %= denominator;
    }

    return res;
}

int main() {
    // int n = 1234;
    // cout << removeFirstDigit(n) << endl;
    int n = 10;
    int m = 3;
    cout << fractionToDecimal(n, m) << endl;
    return 0;
}