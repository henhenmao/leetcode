
/*
225. Implement Stack Using Queues (https://leetcode.com/problems/implement-stack-using-queues/description/)
Follow-up: Can you implement the stack using only one queue?

stack can be implemented with two queues
q1 is the main queue that will emulate a stack
q2 will be a queue on standby for when the push function is called

other stack functions like pop(), top(), and empty() can be easily replaced with queue pop, queue front, and queue empty
main issue is the implementation of push

push(x) example
    let q1 = {1,2,3,4,5}, and the front of the queue represent the top of the stack
    q1.push(6) -> q1 = {6,1,2,3,4,5}
        we use a second queue to assist in moving the 6
        q1 = {1,2,3,4,5}
        q2 = {}
        move all elements from q1 to q2
        q1 = {}
        q2 = {1,2,3,4,5}
        add 6 to q1
        q1 = {6}
        q2 = {1,2,3,4,5}
        add all elements from q2 back to q1
        q1 = {6,1,2,3,4,5}
        p2 = {}

    1. move all elements from q1 to q2
    2. add the pushed value x to q1. q1 now just consists of x at the front of the queue
    3. add all elements from q2 back to q2

pop()
    save the front of the queue to a variable, pop from the queue (does not return a value), and return the saved variable

top()
    just return front of the queue

empty()
    use built in queue empty function

runtime: O(n) for push(), O(1) for all other functions
    where n is the size of the queues
space: O(n)
*/

#include <iostream>
#include <queue>
using namespace std;

class MyStack {

private:
    queue<int> q1, q2; // setting q1 and q2 as class memeber variables

public:
    MyStack() { // front of the queue = top of stack

    }
    
    void push(int x) { // get x to the front of the queue
        while (!q1.empty()) {
            q2.push(q1.front());
            q1.pop();
        }

        q1.push(x);

        while (!q2.empty()) {
            q1.push(q2.front());
            q2.pop();
        }
    }
    
    int pop() { // save front of queue before popping and return 
        int top = q1.front();
        q1.pop();
        return top;
    }
    
    int top() { // front
        return q1.front();
    }
    
    bool empty() {
        return q1.empty();
    }
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */