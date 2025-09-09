


"""
3021. Alice and Bob Playing Flower Game (https://leetcode.com/problems/alice-and-bob-playing-flower-game/description/?envType=daily-question&envId=2025-08-31)

since each player can pick from any of the two lanes on their turn, the only thing that actually matters in determining a winner
is the total number of flowers in both lanes and whoever goes first

person who picks the last flower wins
if there is an odd number of flowers in total
    the person who moves first will always win

since alice goes first and must always win the game:
    total number of flowers must always be an odd number

find the possible pairs of x and y that add up to an odd number pretty much is the question
    given the constraints of 1 <= x <= n and 1 <= y <= m

    should be just = (nm)/2

runtime: O(1)
space: O(1)

"""

def flowerGame(n: int, m: int) -> int:
    return (n * m)//2
