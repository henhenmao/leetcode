
/*
1353. Maximum Number of Events That Can Be Attended (https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/description/?envType=daily-question&envId=2025-07-07)

this is a sorting / heap problem

we want to attended as many events as possible
    this means out of all events that we can attend (events with start days before the current day),
        we should attend the event with the earliest end day
    this will allow us to greedily pick the event that leads to the maximum number of events we can take


algorithm:
    1. sort the events by start day (first index)
    2. create a min heap for the end days of each event
    3. for each day, look at all events that are able to be attended (events that have started but haven't ended)
    4. from those days, choose to attend the event that ends the earliest

runtime: O(n * log(n)) where n is the size of events
    sorting takes n * log(n) and total heap operations are n * log(n)
space: O(n) min heap
*/


#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>
using namespace std;


int maxEvents(vector<vector<int>>& events) {

    sort(events.begin(), events.end());
    priority_queue<int, vector<int>, greater<int>> heap; 

    int day = 0;
    int i = 0;
    int n = events.size();
    int count = 0;

    while (i < n || !heap.empty()) {
        // if no events in heap, go to the next event's start day
        if (heap.empty()) {
            day = events[i][0];
        }

        // add all elements starting today or earlier to the heap
        while (i < n && events[i][0] <= day) {
            heap.push(events[i][1]); // push the end day of selected days
            i++;
        }

        // remove elements that have expired
        while (!heap.empty() && heap.top() < day) {
            heap.pop();
        }

        if (!heap.empty()) {
            heap.pop();
            count++;
            day++; // only one event / day
        } else if (i < n) {
            // go to the start day of the next event if nothing to do today
            day = events[i][0];
        }
    }
    return count;
}


int main() {



    return 0;
}