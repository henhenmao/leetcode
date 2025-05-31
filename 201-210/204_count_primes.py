
import math

"""
204. Count Primes (https://leetcode.com/problems/count-primes/)

i really like this question

initial intuition:
    count every prime there is in one go and then just return all
    primes that are less than n

i just remembered a really cool thing that i can do
for every number like 2 and 3 (d), mark every multiple of that number from d to n as
not prime

the solution requires something called the sieve of eratosthenes (cool name)
https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

idk how to make it faster i'm happy with this solution

algorithm:
    1. create an array primes of size n, where primes[i] is whether or not i is a prime number or not
        assume all numbers in primes are prime at first
    2. starting with i = 2, set all multiples of i to False, and increment i
        since we now all multiples of a number greater than 1 cannot be prime
        make sure not to mark i itself as prime
    3. if i is already marked as not prime, you can skip it as there is no need to do anything anymore
        all multiples of 4 would have been marked by multiples of 2 if you think about it
        if a number is already marked as not prime, you can be sure that all of it's multiples are marked as well
    4. keep incrementing i until sqrt(n) because afterwards is unnecessary
    5. return the number of trues still remaining in primes

runtime: O(n * log(log(n))) i'm not smart enough to understand the math behind this runtime
    according to google the runtime of the sieve is O(n * log(log(n)))

space: O(n)

"""


def countPrimes(n: int) -> int:

    primes = [True] * (n) # indexed from 1 to n-1

    i = 2
    while i < int(math.sqrt(n))+1:
        if not primes[i]:
            i += 1
            continue

        p = i
        j = i+p
        while j < len(primes):
            primes[j] = False
            j += p
        i += 1


    return (primes[2:].count(True))