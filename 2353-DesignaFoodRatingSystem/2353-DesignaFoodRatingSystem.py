# Last updated: 9/17/2025, 10:55:22 PM
from sortedcontainers import SortedSet

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.cuisine_food_map = defaultdict(SortedSet)
        self.cuisines = {}
        self.ratings = {}

        for i in range(len(foods)):
            self.cuisine_food_map[cuisines[i]].add((-ratings[i], foods[i]))
            self.cuisines[foods[i]] = cuisines[i]
            self.ratings[foods[i]] = ratings[i]

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.cuisines[food]
        rating = self.ratings[food]

        self.cuisine_food_map[cuisine].remove((-rating, food))
        self.cuisine_food_map[cuisine].add((-newRating, food))

        self.ratings[food] = newRating
        

    def highestRated(self, cuisine: str) -> str:
        return self.cuisine_food_map[cuisine][0][1]
        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)