
/*
2438. Range Product Queries of Powers (https://leetcode.com/problems/range-product-queries-of-powers/description/?envType=daily-question&envId=2025-08-11)
Since the result can be very large, return it modulo 10^9 + 7.

create the array by taking binary representation of n to get the minimum number of powers of 2 that sum to n
sort the array in non-decreasing order
do a prefix sum solution to find the ranges of i to j
    zero cannot exist since they are not a possible power of 2 that sum to n

i tried a prefix sum solution but i guess im just not smart enough so i'm just gonna brute force it
the modulo thing is absolutely cooking me apparantly i need to use some fermat's theorem according to chatgpt

number of bits will at most be like 30
queries.length < 10^5
brute force is a viable solution i guess

i cannot say that this was an enjoyable experience

algorithm:
    1. create an array of the minimum number of powers of 2 that sum to n from the binary representation of n
        bitset<32> bits(n) gives the binary representation
        loop over the bitset and add each bit value to the array

    2. brute force through each query in queries
        just for each query pair in queries just loop from indices query[0] to query[1] in nums
        make sure to mod every single operation by 10^9 + 7 so that your integer doesn't overflow
        add each product to the result vector

runtime: O(m), where m is the number of queries
    n doesn't matter because it will always be max 32 i think
space: O(1)

*/

#include <iostream>
#include <vector>
#include <bitset>
using namespace std;

vector<int> productQueries(int n, vector<vector<int>>& queries) {
    vector<int> products;
    bitset<32> bits(n);
    vector<int> nums;

    int mod = pow(10, 9) + 7;

    // cout << bits << endl;
    // BITS ARE INDEXED FROM LSB TO MSB DO NOT TRUST THE PRINT STATEMENTS
    for (int i = 0; i < bits.size(); i++) {
        if (bits[i]) {
            nums.push_back(1 << i); // shift bits insteasd of using pow is safer
        }
    }

    // nums is already in sorted order at this point

    for (const auto& pair : queries) {
        int a = pair[0];
        int b = pair[1];

        long long tmp = 1;
        for (int i = a; i <= b; i++) {
            tmp = (tmp * (nums[i] % mod)) % mod;
        }

        products.push_back(tmp % mod);
    }

    return products;
}

int main() {
    int n = 15;
    vector<vector<int>> queries = {{0,1}, {2,2}, {0,3}};
    vector<int> res = productQueries(n, queries);

    for (int n : res) {
        cout << n << " "; 
    }
    cout << endl;

    return 0;
}