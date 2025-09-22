
from typing import List
import heapq
from collections import defaultdict

"""
1912. Design Movie Rental System (https://leetcode.com/problems/design-movie-rental-system/?envType=daily-question&envId=2025-09-17)

need to keep track of the unrented and rented movies at all times

search():
    - want the 5 shops with the cheapest unrented copy of a movie
    - sorted in ascending order with the following priorities:
        1. price
        2. shop id
    - use a min heap storing (price, shopid) for each movie

    keep a hashmap that maps key value pairs of movie : heap containing (price, shop)
    search function can take the first 5 elements of the heap matching to the corresponding movie
    since the rent function exists, make sure the 5 movies popped from the head of the heap actually exist in the state of being unrented

rent():
    - mark a given movie at a given shop as rented
    
    add the movie to the rented heap
    

drop():
    - mark a given movie at a shop as unrented
    - drop will only be called to undo the effects of rent()
        - as in you cannot a movie from shop A and drop it off at shop B

report():
    - want the 5 cheapest rented movies (that may all share the same name)
    - need to return the top 5 cheapest movies as [shop, movie], including the shop it was rented from
    - sorted in ascending order with the following priorities:
        1. price
        2. shop id
        3. movie id

    use a min heap storing (price, shop id, movie id) for all rented movies
    since movies can be dropped off (unrented), make sure the 5 movies popped form the head of the heap actually exist in the state of being rented

two hashmaps
    one for unrented movies
    one for rented movies

each hashmap will have a key value pair of a         


"""


class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.unrentedMovies = {}
        self.unrentedHeaps = {}
        self.rentedMovies = {}
        self.rentedHeap = []

        for shop, movie, price in entries:

            # adding (shop, movie) : price to the list of all unrented movies
            self.unrentedMovies[(shop, movie)] = price

            # adding movie : (price, shop) to the proper heaps in unrentedHeaps
            if movie in self.unrentedHeaps:
                heapq.heappush(self.unrentedHeaps[movie], (price, shop))
            else:
                self.unrentedHeaps[movie] = [(price, shop)]
            
    def search(self, movie: int) -> List[int]:
        if movie not in self.unrentedHeaps:
            return []
        return [shop for _, shop in self.unrentedHeaps[movie][:5]]

    def rent(self, shop: int, movie: int) -> None:
        price = self.unrentedMovies[(shop, movie)]
        self.rentedMovies[(shop, movie)] = price

        heap = self.unrentedHeaps[movie]
        heap.remove((price, shop))
        heapq.heapify(heap)
        heapq.heappush(self.rentedHeap, (price, shop, movie))
        del self.unrentedMovies[(shop, movie)]

    def drop(self, shop: int, movie: int) -> None:
        price = self.rentedMovies[(shop, movie)]
        self.unrentedMovies[(shop, movie)] = price

        heapq.heappush(self.unrentedHeaps[movie], (price, shop))
        self.rentedHeap.remove((price, shop, movie))
        heapq.heapify(self.rentedHeap)
        del self.rentedMovies[(shop, movie)]

    def report(self) -> List[List[int]]:
        return [[shop, movie] for price, shop, movie in self.rentedHeap[:5]]
    
movie = MovieRentingSystem(3, [[0, 1, 5], [0, 2, 6], [0, 3, 7], [1, 1, 4], [1, 2, 7], [2, 1, 5]])

# print(movie.search(1))

print(movie.unrentedMovies)
print(movie.unrentedHeaps)
print()
print(movie.rentedMovies)
print(movie.rentedHeap)
print()

movie.rent(0, 1)
movie.rent(1, 2)

print(movie.unrentedMovies)
print(movie.unrentedHeaps)
print()
print(movie.rentedMovies)
print(movie.rentedHeap)
print()

print(movie.report())

movie.drop(1, 2)

# print(movie.unrentedMovies)
# print(movie.unrentedHeaps)
# print()
# print(movie.rentedMovies)
# print(movie.rentedHeap)
# print()

print(movie.search(2))

