


/*
1925. Count Square Sum Triples (https://leetcode.com/problems/count-square-sum-triples/?envType=daily-question&envId=2025-12-08)

naive approach that works due to the small contraint (O(n^3))
    simply loop every combination of three numbers between 1 and n (1 <= n <= 250)
    check if a*a + b*b == c*c
    count the totals

slightly better approach (O(n^2)!!!)
    loop each pair of a and b
    since a*a + b*b == c*c
    check if sqrt(a*a + b*b) exists as an integer between 1 and n
        if true, add to total

runtime: O(n^2)
space: O(1)
*/

#include <iostream>
using namespace std;

// int countTriples(int n) {
//     int res = 0;

//     for (int i = 1; i <= n; i++) {
//         for (int j = 1; j <= n; j++) {
//             for (int k = 1; k <= n; k++) {
//                 if (i*i + j*j == k*k) {
//                     res += 1;
//                 }
//             }
//         }
//     }

//     return res;
// }

int countTriples(int n) {
    int res = 0;
    
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            double c = sqrt(i*i + j*j);
            if (c >= 1 && c <= n && (int) c == c) {
                res += 1;
            }
        }
    }
    return res;
}


int main() {

    cout << countTriples(10) << endl;

    return 0;
}