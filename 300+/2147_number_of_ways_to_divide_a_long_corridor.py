

"""
2147. Number of Ways to Divide a Long Corridor (https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/?envType=daily-question&envId=2025-12-14)

every single seat should be paired up with the exact same other seat in all possible division scenarios
    the addition of plants between seats simply add more options to divide from while dividing the same seats

1. first pair up each seat to its seat pair
    the string should be divided into sections that begin with the first seat and end with the second seat

    S S P P S S -> (S S) P P (S S)

2. in between the two seat pairs in above example, there are plants
    we need to count how many plants are between the seat pairs
    there are two plants in between in the example
        we can place a divider to the left of the first plant, in the middle of the two plants, or to the right of the second plant

    S S|P P S S
    S S P|P S S
    S S P P|S S

    let k = the number of plants between two adjacent seat pairs
    therefore the number of ways to divide two adjacent seat pairs = k+1


3. if there are multiple seat pairs

    S S P P S S P P S S -> (S S) P P (S S) P P (S S)

    we know that each seat is paired up with the exact same other seat in all possible division scenarios
    with this information we can deduce that in between any two adjacent seat pairs, there is only one division that needs to be made
    therefore we simply calculate the k+1 divisions between all adjacent plant pairs, and return the product of all of them

    S S P P S S P P S S
    we know that S S P P S S has three possible divisions
    but in this example there are two cases of S S P P S S
    so this example would return 3 * 3 = 9

runtime: O(n) where n is the size of corridor
space: O(n)


"""

def numberOfWays(corridor: str) -> int:
    MOD = 10**9+7
    n = len(corridor)

    # no possible divisions if there are an odd number of seats
    seats = corridor.count("S")
    if seats <= 1 or seats % 2 == 1:
        return 0
    
    # if there are only two seats, no dividers can be installed -> single scenrario
    if seats == 2:
        return 1


    # gathering the index of each seat pair into pairs
    # pairs[i] = [index of first seat, index of second seat] 
    pairs = []
    foundFirst = False
    for i in range(n):
        curr = corridor[i]

        if curr == "S":
            if not foundFirst:
                first = i
                foundFirst = True
            else:
                pairs.append([first, i])
                foundFirst = False


    total = 1

    # counting the number of plants between each adjacent seat pair
    for i in range(1, len(pairs)): # i is the second of the two pairs
        pair1 = pairs[i-1]
        pair2 = pairs[i]

        plantCount = pair2[0]-pair1[1] # number of elements (plants) between the end of the first pair and the start of the second pair
        total = (total * plantCount) % MOD

    return total

corridor = "PPSPSP"
print(numberOfWays(corridor))
