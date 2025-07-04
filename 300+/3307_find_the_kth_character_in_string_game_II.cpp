

/*
3307. Find the K-th Character in String Game II (https://leetcode.com/problems/find-the-k-th-character-in-string-game-ii/description/?envType=daily-question&envId=2025-07-04)

since the value of k can go up to 10^14, we cannot simulate this with strings as it will definitely lead to a memory limit problem
because of this, we need to take advantage of the fact that the string always starts at "a" and doubles in size at every operation

the key thing to realize for this problem:
    ex. operations = [0, 1, 0, 1], k = 10
    s = "aabb aabb bbcc bbcc" (split into groups of four for easier reading)
          ^         ^    
                  k = 10
    notice how k=10 is in the second half of the string
    this means that we can find the character that came before k=10, when the s.length() was only 8
    in this case, that character is k=2, since when the last operation was performed
        s went from "aabb aabb" to "aabb aabb bbcc bbcc", and the 'a' at k=2 was incremented to 'b'
    
knowing this, we need to find at every part of the operations, at each different size of s, whether or not
k is at the first half or the second half
    we don't care if k is in the first half

let n be the number of operations made on the initial "a" string
the total size of the string at the end, if we were to simulate it, would be 2^n
since we are doubling the string size at every operation

create a vector firstHalves where firstHalves[i] represents whether or not k is in the second half at s.length() = 2^(n-i)
    (maybe i should have named it better)
since we are starting at 2^(n-i) and working backwards to s.length() == 1, we reverse the vector after building it


finally, with the vector of stages where k is in the second half, and the vector of operations performed,
we can trace our steps to find the kth element when the string game is played

firstHalves and operations should have the same length if everything works properly
loop through both firstHaves and operations with index i
    if both firstHalves[i] is true and operations[i] is 1, we know that the kth character was updated and letter incremented
    if one of the two values is false, k is in the first half or the first operation was made, we know that the kth
    character could not have changed, even after an operation, so we do nothing

we make sure to update k after each successful letter update

to summarize, we are basically counting the number of times the kth character is updated from the initial "a" value.

runtime: O(n) where n is the number of operations made
    even though k goes up to 10^14, we do log(k) operations which is max like = 50 i guess
space: O(n)

*/


#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

char kthCharacter(long long k, vector<int>& operations) {
    // calculate the highest power of two
    // long long size = 1;
    int n = operations.size();

    __int128 size = pow(2, n);

    // create vector of whether or not k is in the first half or second half in each size of power of two
    vector<bool> firstHalves(n, false);

    int i = 0;
    while (i < firstHalves.size()) {
        if (k > size/2) { // second half
            firstHalves[i] = true;
            k -= size/2;
        }
        size /= 2;
        i += 1;
    }

    // for (bool b : firstHalves) {
    //     cout << b << ", ";
    // }

    reverse(firstHalves.begin(), firstHalves.end());

    char a = 'a';
    for (int i = 0; i < n; i++) {
        if (firstHalves[i] && operations[i]) {
            a = (a == 'z') ? 'a' : a+1;
        }
    }

    return a;
}

int main() {
    long long k = 10;
    vector<int> operations = {0, 1, 0, 1};
    cout << kthCharacter(k, operations); 

}