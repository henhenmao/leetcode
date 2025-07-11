

/*
274. H-Index (https://leetcode.com/problems/h-index/description/?envType=study-plan-v2&envId=top-interview-150)

https://en.wikipedia.org/wiki/H-index - definition of H-index

it is probably a good idea to sort the citations for each of the researcher's papers

ex. citations = [3,0,6,1,5] -> sort -> [0,1,3,5,6]
    iterate through the citations with a 


god help us all

*/

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;



int hIndex(vector<int>& citations) {
        
}


int main() {
    vector<int> citations = {3, 0, 6, 1, 5};
    cout << hIndex(citations) << endl;
    return 0;
}