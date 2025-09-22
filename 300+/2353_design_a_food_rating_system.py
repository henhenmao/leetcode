
from typing import List
import heapq

"""
2353. Design a Food Rating System (https://leetcode.com/problems/design-a-food-rating-system/description/?envType=daily-question&envId=2025-09-17)

have a hashmap containing pairs of food names to their corresponding (cuisine ratings)
have another hashmap containing pairs of cuisine types to a heap containing all ratings of that cuisine

FoodRatings()
    initialize the two hashmaps
    for each food, add the pair of food : (cuisine, rating) to the first hashmap
    in the second hashmap, add the pair of (-rating, food) to the proper heap with the matching cuisine
        put in the rating as -rating so that the maximum rating gets priority
        make sure the -rating goes first because the first element of the tuple is prioritizes
        if the cuisine does not yet exist as a key, create a new heap
    
changeRating()
    retrieve the info of the food from the first hashmap
    easily edit the rating in the foodrating hashmap with the new rating replacing the current one
    add the new rating and cuisine to the second hashmap, disregarding the current rating being replaced

highestRated()
    select the heap of the selected cuisine
    retrieve the top of the heap with the highest rating
    check if the food with the highest rating matches with the food in foodratings
    if match, return that food
    if no match, pop from the heap

runtime:
    FoodRatings(): O(n) where n is the size of the three lists
    changeRating(): O(1)
    highestRated(): O(log n)

space: O(n)
"""


class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foodratings = {}
        self.cuisineratings = {}

        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.foodratings[food] = (cuisine, rating)
            if cuisine not in self.cuisineratings:
                self.cuisineratings[cuisine] = []
            heapq.heappush(self.cuisineratings[cuisine], (-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine, _ = self.foodratings[food]
        self.foodratings[food] = (cuisine, newRating)
        heapq.heappush(self.cuisineratings[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        heap = self.cuisineratings[cuisine]
        while heap:
            rating, food = heap[0]
            if self.foodratings[food][1] == -rating:
                return food
            heapq.heappop(heap)
        return ""
    

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)