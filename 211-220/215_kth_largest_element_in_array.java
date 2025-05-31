
import java.util.*;

/*
215. Kth Largest Element in an Array (https://leetcode.com/problems/kth-largest-element-in-an-array/)

we need to find the kth largest number in an array without sorting
the without sorting part is what makes the question difficult
thankfully, there is a particular data structure that maintains specific ordering properties

max heap:
    a max heap is a data structure that has the following properties:
        1. is a complete binary tree - all levels are filled
        2. heap property - for every single node other than the parent, the value of the parent node is
            greater than or equal to the value of that node

we can use the max heap property to find the kth largest element in the list

java's PriorityQueue class is a heap based queue that stores elements based on their priority instead of the standard first in first out order of a queue
    by default, elements with lower values have higher priority (min heap)
    we can use a method or a comparator to change the priority queue into a max heap instead


algorithm:
    1. create priorityqueue and set to prioritize max values
    2. add all values in nums into the priority queue
    3. remove the head of the maxHeap k-1 times
    4. return the head of the maxHeap

runtime: O(n * log(k)) a priority queue takes log(k) time to insert items into a queue of size k
    we are doing a log(k) insertion for every elemenet in nums 
space: O(k) storing k elements at most

*/

class Solution {
    public int findKthLargest(int[] nums, int k) {

        // creates a PriorityQueue
        // uses a comparator to change the priority from min to max
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(
            (a, b) -> {return b-a;}
        );

        // adding all elements from nums to maxHeap
        for (int n : nums) {
            maxHeap.offer(n);
        }

        // removing the first k-1 elements
        for (int i = 0; i < k-1; i++) {
            maxHeap.poll();
        }

        return maxHeap.peek();


    }
}