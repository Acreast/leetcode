# Last updated: 12/4/2025, 11:19:59 PM
1class Solution:
2    def countCollisions(self, directions: str) -> int:
3        directions = directions.lstrip("L")
4        directions = directions.rstrip("R")
5
6        return directions.count("R") + directions.count("L")
7        
8